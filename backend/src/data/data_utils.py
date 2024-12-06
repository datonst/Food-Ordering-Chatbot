import pandas as pd
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

def create_user(db: Session, username: str, fullname: str, email: str, password: str):
    db_user = Users(username = username, email=email, fullname=fullname, password = password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

