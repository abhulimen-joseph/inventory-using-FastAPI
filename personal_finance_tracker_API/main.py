import models
import schemas
import database
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
models.Base.metadata.create_all(bind = database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_balance(db:Session):
    total_income = db.query(func.sum(models.Income.amount).scalar())
    total_expenses = db.query(func.sum(models.Expenses.amount).scalar())
    return total_income - total_expenses

@app.get("/balance")
def get_balance(db: Session = Depends(get_db)):
    balance = calculate_balance(db)
    return {f"Balance: {balance}"}

@app.get("/")
def root():
    return {"message": "Finance API"}

@app.post("/income/", response_model=schemas.FinanceResponseIncome)
def create_income(income: schemas.FinanceCreateIncome, db: Session= Depends(get_db)):
    db_income = models.Income(**income.model_dump())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

@app.get("/income/", response_model=list[schemas.FinanceResponseIncome])
def get_income(db: Session= Depends(get_db)):
    db_allIncome = db.query(models.Income).all()
    if db_allIncome is None:
        raise HTTPException(status_code=404, detail="Income not found")
    return db_allIncome

@app.post("/expenses/", response_model=schemas.FinanceResponseExpense)
def create_expense(expense: schemas.FinanceCreateExpense, db: Session = Depends(get_db)):
    db_expense = models.Expenses(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses/", response_model=list[schemas.FinanceResponseExpense])
def all_expenses(db: Session = Depends(get_db)):
    db_allexpenses = db.query(models.Expenses).all()
    if db_allexpenses is None:
        raise HTTPException(status_code=404, detail= "Expenses does not exist ")
    return db_allexpenses

@app.get("/expenses/{expense_id}", response_model=schemas.FinanceResponseExpense)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail= "Expense not found")
    return expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail= "Expense not found")
    db.delete(expense)
    db.commit()

    return {f"detail: expense_id {expense_id} has been deleted"}

@app.put("/expense/{expense_id}", response_model =schemas.FinanceResponseExpense)
def update_expense(expense_id: int, expense_update: schemas.FinanceUpdateExpense, db:Session = Depends(get_db)):
    expense = db.query(models.Expenses).filter(models.Expenses.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="invalid Expense id")
    
    update_data = expense_update.dict(exclude_unset = True)

    for field, value in update_data.items():
        setattr(expense, field, value)

    db.commit()
    db.refresh(expense)

    return expense

