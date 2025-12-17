from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import Field, BaseModel

#pydynatic model
class Item(BaseModel):
    name: str = Field(min_length=3, max_length=50, examples="cloth")
    price: float = Field(gt=0, examples=1200.00)
    available: bool = True
    quantity: Optional[int] = Field(default=None, gt=0, examples=50)

inventory_db: List[Item] = []
current_db = 0

# now i'm putting fastAPi application
app = FastAPI(
    title = "Simple inventory management",
    description = "A basic CRUD API demonstrating FastAPI and Pydantic."
)

# test if the application is successfully working 
@app.get("/")
async def welcome():
    return{"message": "Inventory API is running. Check postman for the endpoints"}

# to create a items in the list 
@app.post("/items/", response_model= Item, status_code=201)
async def create(item: Item):
    global current_db
    inventory_db.append(item)
    current_db +=1
    return item
