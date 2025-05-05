from sqlalchemy.orm import Session
import app.models
import app.schemas
from datetime import datetime

from app import models, schemas


def get_books(db: Session):
    return db.query(models.Book).filter(models.Book.is_deleted == False).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    data = book.dict(exclude_unset=True)
    data["updated_date"] = datetime.utcnow()
    db_book = models.Book(**data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_data: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book_data.dict().items():
            setattr(db_book, key, value)
        db_book.updated_date = datetime.utcnow()
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.is_deleted = True
        db.commit()
    return db_book