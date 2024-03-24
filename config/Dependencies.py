from config.db import SessionLocal
from passlib.context import CryptContext


# The below function is used to database session


def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# The below function is used for password Hashing


pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")


def bcrypt(password: str) :
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
