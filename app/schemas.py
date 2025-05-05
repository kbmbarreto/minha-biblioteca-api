from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    publishing_company: str = Field(..., alias="publishingCompany")
    is_readed: bool = Field(False, alias="isReaded")
    is_digital: bool = Field(False, alias="isDigital")
    is_deleted: Optional[bool] = Field(False, alias="isDeleted")
    cover: Optional[str] = ""
    updated_date: Optional[datetime] = None

    class Config:
        populate_by_name = True
        orm_mode = True

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int