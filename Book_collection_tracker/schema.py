from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None
    rating: Optional[int] = None
    
class BookUpdate(BookCreate):
    title: Optional[str] = None
    author: Optional[str] = None

class BookResponse(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes= True)