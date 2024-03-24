from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.Dependencies import get_db, bcrypt
from models.books import User
from schemas.Books import UserSchema

# ===================================================================

# Below method is to get all Users


def get_all(db: Session = Depends(get_db)):
    books = db.query(User).all()
    return books

# ===================================================================

# Below method is used to create user


def create_user(request = UserSchema, db: Session = Depends(get_db)):
    new_user = User(
        name = request.name,
        email = request.email,
        password = bcrypt(request.password)

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ===================================================================

# Below method is used to get user by id


def get_user(id: int,  db: Session = Depends(get_db)):
    _User = db.query(User).filter(User.id == id).first()

    if not _User:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'user with id {id} not found')
    return _User
