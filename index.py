from fastapi import FastAPI
from routes import Book, User, authentication
import uvicorn


app = FastAPI()


# Add your FastAPI routes here


app.include_router(authentication.router)
app.include_router(Book.router)
app.include_router(User.router)


if __name__ != "__main__":
    pass
else:
    uvicorn.run(app, host="localhost", port=8000)
