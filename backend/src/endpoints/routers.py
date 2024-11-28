import dotenv
dotenv.load_dotenv()



"""File containing root routes"""
from fastapi.routing import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status, Form
from fastapi import File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Định nghĩa oauth2_scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


from fastapi import status
from typing import Annotated
import base64
import httpx
import asyncio
import copy
import json
import tempfile
import uuid
import jwt
from pathlib import Path
from datetime import datetime, timedelta
from jose import JWTError
from typing import Optional


# Schemas
from src.schemas import FunctionCall
from src.schemas import (
    ChatRequest,
    FunctionCall,
    AudioTranscriptRequest,
    AudioTTSRequest,
    Login,
    Register,
    UpdateProfile,
    Token,
    TokenData,
)
from src.handlers import MainHandler
from src.data.data_models import Restaurant, Foods, Users
from src.schemas import base_models
from src.utils.security import hash_password, verify_password

# Services
from src.services import openai_service, functions
from src.services.user_services import authenticate_user, create_access_token, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, get_user_by_token, verify_token

# Data
from sqlalchemy.orm import Session
from src.data.data_utils import get_db
from sqlalchemy.orm import Session

from src.data.data_utils import get_db, create_user

def create_router(handler: MainHandler, CONFIG):
    router = APIRouter()
    client = handler.openai_client

    ## Question answering
    @router.post("/chat/send_message")
    async def send_message(prompt_request: ChatRequest):
        """Receives the chatlog from the user and answers"""

        # Initializes the handler
        prompt_handler = handler.prompt_handler
        
        # Collects the messages in a list of dicts
        messages = prompt_handler.get_messages(prompt_request)

        # For function calling functionality
        functions = []
        if prompt_request.function_call:
            functions = prompt_handler.get_functions()
        
        try:
            # Calls the main chat completion function

            prompt_response = await openai_service.chat_completion(
                messages=messages,
                CONFIG=CONFIG,
                functions=functions,
                client=client
            )

            # Formats and returns
            response = prompt_handler.prepare_response(prompt_response)

        except Exception as e:
            print(e)
            response = {"response": "Oops there was an error, please try again", "function_call": None}

        return response
    
    @router.post("/chat/function_call")
    async def function_call(function_call: FunctionCall):
        """Receives the function call from the frontend and executes it"""

        # Preparing functions
        function_call_properties = jsonable_encoder(function_call)
        function_name = function_call_properties["name"]
        function_arguments = json.loads(function_call_properties["arguments"])

        # Configuring functions to be called - it should match the get_functions_signatures, otherwise we need to bypass it
        available_functions = {
            # Obs: all functions need to be async
            "get_restaurant_pages": lambda kwargs: functions.find_restaurant_pages(CONFIG=CONFIG, **kwargs),
            "open_restaurant_page": lambda kwargs: functions.open_restaurant_page(CONFIG=CONFIG, **kwargs),
            "close_restaurant_page": lambda _: functions.dummy_function(), # dummy function - no need of information
            "get_user_actions": lambda _: functions.dummy_function(), # dummy function - actions are stored in the frontend
            "get_menu_of_restaurant": lambda kwargs: functions.get_menu_of_restaurant(CONFIG=CONFIG, **kwargs),
            "add_food_to_cart": lambda kwargs: functions.add_food_to_cart(CONFIG=CONFIG, **kwargs),
            "remove_food_from_cart": lambda kwargs: functions.remove_food_from_cart(CONFIG=CONFIG, **kwargs),
            "open_shopping_cart": lambda _: functions.dummy_function(), # dummy function - no need of information
            "close_shopping_cart": lambda _: functions.dummy_function(), # dummy function - no need of information
            "place_order": lambda _: functions.dummy_function(), # dummy function - no need of information
            "activate_handsfree": lambda _: functions.dummy_function(), # dummy function - no need of information
        }

        # Calling the function selected
        function_response = await available_functions[function_name](function_arguments)

        return {"response": function_response}

    @router.post("/chat/transcribe")
    async def generate_transcription(audio_req: AudioTranscriptRequest):
        """Receives the audio file from the frontend and transcribes it"""

        # Initializes the handler
        audio_handler = handler.audio_handler
        
        # Extracts the audio segment of the file
        audio_segment, _ = audio_handler.extract_audio_segment(audio_req.audio)

        # Send it as a tempfile path to openai - because that's the acceptable way to do it
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as tmp_file:
            audio_segment.export(tmp_file.name, format="mp3")
            speech_filepath = Path(tmp_file.name)
            transcripted_response = await openai_service.whisper(audio_file=open(speech_filepath, "rb"), CONFIG=CONFIG, client=client)

        return {"response": transcripted_response}

    @router.post("/chat/tts")
    async def generate_tts(tts_req: AudioTTSRequest):
        """Receives the text from the frontend and generates the audio file"""

        # Generates the audio file
        audio = await openai_service.tts(text=tts_req.text, CONFIG=CONFIG, client=client)

        return {"response": audio}

    ## Retrieving from the database
    @router.get("/restaurants/")
    def get_restaurants(db: Session = Depends(get_db)):
        return db.query(Restaurant).all()
    
    @router.get("/restaurants/{restaurant_id}/foods/")
    def get_foods_from_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
        restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        foods = db.query(Foods).filter(Foods.restaurant_id == restaurant_id).all()
        return foods

    @router.post("/login", response_model=None)
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),  
    ) -> Token:
        user = authenticate_user(db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")
    @router.post("/register")
    async def register(
        username: str = Form(...),
        fullname: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
    ):
        # Kiểm tra xem username đã tồn tại chưa
        existing_username = db.query(Users).filter(Users.username == username).first()
        if existing_username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists."
            )

        # Kiểm tra xem email đã tồn tại chưa
        existing_useremail = db.query(Users).filter(Users.email == email).first()
        if existing_useremail:
            raise HTTPException(
                status_code=400,
                detail="Email already exists."
            )

        # Tạo người dùng mới
        create_user(db, username=username, fullname=fullname, email=email, password=password)

        return {
            "message": "User registered successfully.",
            "user": {
                "username": username,
                "email": email
            }
        }
    

    # def get_user_by_token(db: Session, token: str) -> Optional[Users]:
    #     credentials_exception = HTTPException(
    #         status_code=401,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    
    # # Giải mã token và lấy username
    #     username = verify_token(token, credentials_exception)
        
    #     # Truy vấn người dùng từ DB theo username
    #     user = db.query(Users).filter(Users.username == username).first()
        
    #     # Kiểm tra xem người dùng có tồn tại không
    #     if user is None:
    #         raise credentials_exception
    #     return user
    
    # def verify_token(token: str, credentials_exception):
    #     try:
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username: str = payload.get("sub")
    #         if username is None:
    #             raise credentials_exception
    #         return username
    #     except JWTError:
    #         raise credentials_exception
    

    @router.post("/updateProfile")
    async def update_profile(
        token: str = Depends(oauth2_scheme),
        username: str = Form(None),
        email: str = Form(None),
        password: str = Form(None),
        db: Session = Depends(get_db)
    ):
        if not any([username, email, password]):
            raise HTTPException(
                status_code=400,
                detail="At least one field (username, email, or password) must be updated"
            )
        user = get_user_by_token(db, token)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        if username:
            user.username = username
        if email:
            existing_email = db.query(Users).filter(Users.email == email).first()
            if existing_email:
                raise HTTPException(
                    status_code=400,
                    detail="Email already exists"
                )
            user.email = email
        if password:
            # Hàm hash_password phải là một hàm để mã hóa mật khẩu
            user.password = password
        db.commit()
        return {"message": "Profile updated successfully", "user": {"username": user.username, "email": user.email}}
    
    return router