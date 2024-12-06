import dotenv
dotenv.load_dotenv()

import jwt
from jose import JWTError
from typing import Optional



from sqlalchemy.orm import Session
from src.schemas.base_models import Login, Register, UpdateProfile
from src.data.data_models import Users
from src.data import database as db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from datetime import datetime, timedelta, timezone
from src.schemas.base_models import Token, TokenData

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2 = OAuth2PasswordBearer(tokenUrl="/login")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        print("User {user.username} didn't exist")
        return None
    if password != user.password:
        print(f"Wrong password, {password}")
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

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
    
def get_user_by_token(db: Session, token: str) -> Optional[Users]:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Giải mã token và lấy username
    username = verify_token(token, credentials_exception)
    
    # Truy vấn người dùng từ DB theo username
    user = db.query(Users).filter(Users.username == username).first()
    
    # Kiểm tra xem người dùng có tồn tại không
    if user is None:
        raise credentials_exception
    return user
