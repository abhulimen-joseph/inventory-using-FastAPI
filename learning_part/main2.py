from fastapi import FastAPI, HTTPException, Depends
import schema
import models
import database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db

    finally:
        db.close()

@app.post("/items/", response_model=schema.ItemResonse)
def create_item(item:schema.ItemCreate, db: Session= Depends(get_db)):
    db_item = models.itemmodel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=schema.ItemResonse)
def read_item(item_id: int, db: Session= Depends(get_db)):
    item = db.query(models.itemmodel).filter(models.itemmodel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail= "item not found")
    
    return item
    