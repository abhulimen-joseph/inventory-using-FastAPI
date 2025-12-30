import database
import models
from schema import BookResponse,BookCreate, BookUpdate
from fastapi import FastAPI,HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind= database.engine) # to connect the database using the model feature on ow the database is to look like 
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@app.get('/')
def root():
    return {"message": "Book collection API"}

@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/all", response_model=List[BookResponse])
def get_all(db: Session = Depends(get_db)):
    db_allBooks = db.query(models.BookModel).all()
    return db_allBooks

@app.get("/books/{book_id}", response_model = BookResponse)
def get_book(book_id:int, db: Session = Depends(get_db)):
    db_book = db.query(models.BookModel).filter(models.BookModel.id == book_id).first()
    if book_id is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_book

@app.delete("/books/{book_id}", response_model= BookResponse)
def delete_book(book_id:int, db: Session = Depends(get_db())):
    db_book = db.query(models.BookModel).filter(models.BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code = 404, detail="Book not found")
    
    deleted_book = db_book

    if db_book:
        db.delete(db_book)
        db.commit()

    return deleted_book
    

@app.put("/books/{book_id}", response_model=BookResponse)
def update(book_id:int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.BookModel).filter(models.BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code= 404, detail= "Book not found")

    updated_book = book.model_dump(exclude_unset= True)

    for key, value in updated_book.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)

    return db_book
