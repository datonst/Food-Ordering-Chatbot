import sys
sys.path.append('/Users/raiju/chatbot-TTNM/backend')
import pandas as pd
from src.utils.security import hash_password
from sqlalchemy.orm import Session

try:
    from database import SessionLocal
    from data_models import Restaurant, Foods, Users
except:
    from .database import SessionLocal
    from .data_models import Restaurant, Foods, Users


def get_restaurants(db: Session):
    return db.query(Restaurant).all()

def get_foods(db: Session):
    return db.query(Foods).all()

def get_menu_of_given_restaurant(db: Session, restaurant_id: int):
    return db.query(Foods).filter(Foods.restaurant_id == restaurant_id).all()

def create_user(db: Session, email: str, full_name: str, password: str):
    hashed_password = hash_password(password)
    db_user = Users(email=email, full_name=full_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username)

def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

def update_user_profile(db: Session, user_id: int, email: str = None, hashed_password: str = None):
    user = db.query(Users).filter(Users.id == user_id).first()
    if email:
        user.email = email
    if hashed_password:
        user.hashed_password = hashed_password
    db.commit()
    db.refresh(user)
    return user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

