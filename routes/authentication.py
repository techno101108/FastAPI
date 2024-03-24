from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from config.Dependencies import get_db, verify_password
from models.books import User
from repository.token import create_access_token
from schemas.Books import Login

router = APIRouter(tags = ["Authentication"])


@router.post("/login", status_code = status.HTTP_201_CREATED)
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid Credentials")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Incorrect Password")
    # access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data = {"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}