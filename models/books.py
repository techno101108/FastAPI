from sqlalchemy import Column, ForeignKey, Integer, String
from config.db import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "Data_Books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255))
    author = Column(String(255))
    genre = Column(String(255))
    sub_genre = Column(String(255))
    publisher = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates = "Books")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50))
    email = Column(String(255))
    password = Column(String(255))

    Books = relationship("Book", back_populates = "creator")
