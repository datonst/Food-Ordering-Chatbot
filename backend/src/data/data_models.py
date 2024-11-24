from sqlalchemy import Column, Integer, String

try:
    from database import Base
    from sqlalchemy import Column, Integer, String  # hoặc các kiểu dữ liệu cần thiết khác
except:
    from .database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)

class Foods(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)
    price = Column(Integer, index=True)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    fullname = Column(String, nullable = False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)