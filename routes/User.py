import fastapi
from fastapi import status, Depends
from sqlalchemy.orm import Session
from models.index import User
from schemas.index import ShowUser, UserSchema, UserBook
from config.Dependencies import get_db
from repository import User

router = fastapi.APIRouter(tags = ["Users"], prefix = "/api/user")


# Below method is to get all Users


@router.get("/", response_model = list[ShowUser], status_code = status.HTTP_200_OK)
def get_all_user(db: Session = Depends(get_db)) :
    return User.get_all(db)


# Below method is used to add a new user


@router.post("/", status_code = status.HTTP_201_CREATED)
def add_new_user(request: UserSchema, db: Session = Depends(get_db)) :
    return User.create_user(request, db)


# Below method is used to get user by id


@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = UserBook)
def get_user_by_id(id: int, db: Session = Depends(get_db)) :
    return User.get_user(id, db)
