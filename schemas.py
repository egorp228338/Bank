from pydantic import BaseModel, EmailStr
from datetime import datetime


class StorageBase(BaseModel):
    storage_id: int
    storage_address: str

class User(BaseModel):
    user_id: int
    user_name: str
    user_login: int
    user_pass: str
    user_email: str
    user_phone: int

class Record(BaseModel):
    record_id: int
    user_id: int
    book_id: int
    user_email: str
    user_phone: int

class Book(BaseModel):
    book_Id: int
    book_author: str
    book_genre: str
    book_description: str