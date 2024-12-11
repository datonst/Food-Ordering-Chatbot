
try:
    from database import Base, engine
    from data_models import Restaurant, Foods, Users
except:
    from .database import Base, engine
    from .data_models import Restaurant, Foods, Users

def main():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    main()