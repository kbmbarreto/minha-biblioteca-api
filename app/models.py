from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base
from datetime import datetime

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    publishing_company = Column(String(255), nullable=False)
    is_readed = Column(Boolean, default=False)
    is_digital = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    cover = Column(String(255))
    updated_date = Column(DateTime, default=datetime.utcnow)