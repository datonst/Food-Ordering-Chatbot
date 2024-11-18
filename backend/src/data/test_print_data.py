import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Restaurant, Foods, Users

def get_restaurants(db: Session):
    return db.query(Restaurant).all()

def get_foods(db: Session):
    return db.query(Foods).all()

def get_Users(db: Session):
    return db.query(Users).all()

def main():
    db = SessionLocal()

    # Fetch data from the restaurants table
    restaurants = get_restaurants(db)

    # Convert the data to a pandas DataFrame
    restaurant_data = [{"id": r.id, "name": r.name, "description": r.description, "image": r.image} for r in restaurants]
    restaurant_df = pd.DataFrame(restaurant_data)

    # Print the Restaurants DataFrame
    print("Restaurants:")
    print(restaurant_df)

    # Fetch data from the foods table
    foods = get_foods(db)

    # Convert the data to a pandas DataFrame
    food_data = [{"id": f.id, "restaurant_id": f.restaurant_id, "name": f.name, "description": f.description, "image": f.image, "price": f.price} for f in foods]
    food_df = pd.DataFrame(food_data)

    # Print the Foods DataFrame
    print("\nFoods:")
    print(food_df)

    users = get_Users(db)
    user_data = [{"id": u.id, "username": u.username, "email": u.email, "hashed_password": u.hashed_password} for u in users]
    user_df = pd.DataFrame(user_data)

    print("\nUsers")
    print(user_df)
    breakpoint()

if __name__ == "__main__":
    main()