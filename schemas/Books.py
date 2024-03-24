from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    genre: str
    sub_genre: str
    publisher: str


class Book(BookSchema):
    pass

    class Config():
        orm_mode = True


class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config() :
        orm_mode = True


class UserBook(BaseModel):
    name: str
    email: str
    Books: list[Book] = []

    class Config():
        orm_mode = True


class ShowBook(BaseModel):
    title: str
    author: str
    genre: str
    sub_genre: str
    publisher: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
