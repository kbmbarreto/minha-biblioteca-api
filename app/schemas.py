from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    publishing_company: str
    is_readed: bool = False
    is_digital: bool = False
    is_deleted: Optional[bool] = False
    cover: Optional[str] = ""
    updated_date: Optional[datetime] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True