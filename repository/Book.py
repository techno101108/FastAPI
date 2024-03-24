from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from config.Dependencies import get_db
from models.books import Book
from schemas.Books import BookSchema


# Below methods are used to make crud utilities

# Below method is to get all books


def get_all(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

# Below method is used to get  single book


def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()

    if not book :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'user with id {id} not found')
    return book


# Below method is to create a new book


def create_new_book(request: BookSchema, db: Session = Depends(get_db)):
    new_book = Book(
        title = request.title,
        author = request.author,
        genre = request.genre,
        sub_genre = request.sub_genre,
        publisher = request.publisher,
        user_id = 5
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)


# Below method is used to update book


def update_book(id: int, request: BookSchema, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id)

    if not book.first() :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with ID {id} not found')

    book.update(request.dict())
    db.commit()
    return 'Data Updated'

# Below method is to delete a new book


def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id)

    if not book.first() :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Book with ID {id} not found')
    book.delete(synchronize_session = False)
    db.commit()

    return "Book deleted"