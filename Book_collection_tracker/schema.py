from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[str]
    genre: Optional[str]
    rating: Optional[int]
    


class BookResponse(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes= True)