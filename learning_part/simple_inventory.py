from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import Field, BaseModel

#pydynatic model, this how the json is created using this 
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
    current_db +=1
    inventory_db.append(item)
    return item

# this gives the values stored in the list
@app.get("/item/", response_model=List[list])
async def get_items():
    return inventory_db

# to get an element in a the list
@app.get("/items/{item_index}", response_model=Item)
async def get_item(item_index: int):
        if item_index < 0 or item_index >= len(inventory_db):
            raise  HTTPException(status_code=404, detail=f"item at index {item_index} not found")
        return inventory_db[item_index]
    
        
@app.put("/items/{item_index}", response_model=Item)
async def update_item(item_index: int, updated_item: Item):
     if item_index < 0 or item_index >= len(inventory_db):
          raise HTTPException(status_code=404, detail=f"The item at index {item_index} is not found")
     inventory_db[item_index] = updated_item
     return updated_item

@app.delete("/items/{item_index}", status_code=204)
async def delete_item(item_index: int):
     if item_index < 0 or item_index >= len(inventory_db):
          raise HTTPException(status_code=404, detail=f"The index at index {item_index} is not found")
     del inventory_db[item_index]
     return