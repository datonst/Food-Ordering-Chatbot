import sys
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Extend the system path for imports if necessary
sys.path.append('/Users/raiju/chatbot-TTNM/backend')

from src.schemas.base_models import Login, Register, UpdateProfile
from src.services.user_services import register_user, login_user, update_user_profile
from src.data.data_utils import get_db

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Định nghĩa router
router = APIRouter()

@router.post("/register")
async def register(user_data: Register, db: Session = Depends(get_db)):
    try:
        user = register_user(db, user_data)
        return {"msg": "User registered successfully", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(login_data: Login, db: Session = Depends(get_db)):
    try:
        user = login_user(db, login_data)
        return {"msg": "Login successful", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/update-profile")
async def update_profile(user_id: int, update_data: UpdateProfile, db: Session = Depends(get_db)):
    try:
        user = update_user_profile(db, user_id, update_data)
        return {"msg": "User profile updated", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Gắn router vào ứng dụng FastAPI
app.include_router(router)

