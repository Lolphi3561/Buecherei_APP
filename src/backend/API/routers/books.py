from datetime import date

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel, Field, ValidationError, field_validator
from sqlalchemy.orm import Session

from fastapi_restful.cbv import cbv
"""""""""from database import get_db"""""""""
from routers.base import BaseAPI
import models


router = APIRouter(prefix="/books", tags=["Book"])

class BookCreate(BaseModel):

    isbn: str
    title: str
    author: str
    publisher: str
    publishedYear: date
    isAvailable: bool

    @field_validator('author', 'publisher')
    def check_no_digits(cls, value:str):
        if any(char.isdigit() for char in value):
            raise ValidationError("No digits allowed in Names")
        else:
            return value
    

class BookResponse(BookCreate):
    id: int = Field(..., gt=0)


@cbv(router)
class BookAPI(BaseAPI):
    db: JsonStore = Depends(get_file)

    @router.get("/books", response_model=list[BookResponse])
    def getbooks(self):
        return self.db.query(models.BOOKS).all()

    # TODO!!!!!!!!!
    @router.get("/books?q={query}", response_model=list[BookResponse])
    def getbooks(self):
        return self.db.query(models.BOOKS).all()
    # !!!!!!!!!!!

    @router.get("/books/{id}", response_model=BookResponse)
    def getbook_by_id(self, id:int):
        return self.get_or_404(self.db, models.BOOKS, id)
    
    @router.post("/books", response_model=BookResponse)
    def createbook(self, book:BookCreate):
        db_book = models.BOOKS(title = book.title, author = book.author, publisher = book.publisher, publishedYear = DateTime.Year, isAvailable = True)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book


    @router.delete("/{book_id}")
    def delete_book(self, book_id:int):
        db_book = self.get_or_404(self.db, models.BOOKS, book_id)
        self.db.delete(db_book)
        self.db.commit()
        return f"Buch mit Id {book_id} wurde von der Tabelle gelöscht."