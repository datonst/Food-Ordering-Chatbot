import sys
sys.path.append('/Users/raiju/chatbot-TTNM/backend')
import jwt

from sqlalchemy.orm import Session
from src.data.data_utils import get_user_by_username, get_user_by_email, update_user_profile
from src.schemas.base_models import Login, Register, UpdateProfile
from src.utils.security import verify_password
from src.data.data_models import Users
from src.data import database as db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from datetime import datetime, timedelta, timezone
from src.schemas.base_models import Token, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


oauth2 = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def register_user(db: Session, user_data: Register):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("User with this email already exists.")
    return Register(db, user_data.email, user_data.full_name, user_data.password)

def login_user(db: Session, login_data: Login):
    user = get_user_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise ValueError("Invalid credentials.")
    return user

def update_user_profile(db: Session, user_id: int, update_data: UpdateProfile):
    user = db.query(id).filter(id == user_id).first()
    if not user:
        raise ValueError("User not found.")
    return UpdateProfile(db, user, update_data.dict(exclude_unset=True))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user