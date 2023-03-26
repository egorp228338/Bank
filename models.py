from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from database import Base

class Storage(Base):
    tablename = "storage"

    storage_id = Column(Integer, primary_key=True, nullable=False)
    storage_address = Column(String, nullable=False)


class User(Base):
    tablename = "user"

    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    user_login = Column(String, nullable=False)
    user_pass = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    user_phone = Column(Integer, nullable=False)

class Record(Base):
    tablename = "record"

    record_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete = "CASCADE"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.book_id", ondelete = "CASCADE"), nullable=False)
    user_email = Column(String, nullable=False)
    user_phone = Column(Integer, nullable=False)

class Book(Base):
    tablename = "book"
    
    book_id = Column(Integer, primary_key=True, nullable=False)
    book_author = Column(Integer, nullable=False)
    book_genre = Column(String, nullable=False)
    book_description = Column(String, nullable=False)
    
    
    