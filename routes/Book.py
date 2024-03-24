import fastapi
from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import Session
from models.index import Book
from schemas.index import ShowBook, BookSchema
from config.Dependencies import get_db
from config.db import Base, engine
from repository import Book


Base.metadata.create_all(engine)
router = fastapi.APIRouter(tags = ["Books"], prefix = "/api/book")

# ===================================================================

# Below method is to get all books


@router.get("/", response_model = list[ShowBook], status_code = status.HTTP_200_OK)
def get_all_book(db: Session = Depends(get_db)):
    return Book.get_all(db)

# ===================================================================

# Below method is to post a new book


@router.post("/", status_code = status.HTTP_201_CREATED)
def add_new_book(request: BookSchema, db: Session = Depends(get_db)):
    return Book.create_new_book(request,db)

# ===================================================================

# Below method is used to get book by id


@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = ShowBook)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    return Book.get_book(id, db)

# ===================================================================

# Below method is used to update book by id


@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update_book_by_id(id: int, request: BookSchema, db: Session = Depends(get_db)):
    return Book.update_book(id, request, db)

# ===================================================================

# Below method is used to delete the book by id


@router.delete("/{id}", status_code = status.HTTP_200_OK)
def delete_book_by_id(id: int, db: Session = Depends(get_db)):
    return Book.delete_book(id, db)