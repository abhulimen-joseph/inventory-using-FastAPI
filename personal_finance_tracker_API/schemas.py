from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class FinanceCreateIncome(BaseModel):
    date: Optional[date] = None
    amount: int
    source: str
    frequency: Optional[str] = None


class FinanceResponseIncome(FinanceCreateIncome):
    id: int
    date: date
    model_config = ConfigDict(from_attributes= True)

class FinanceCreateExpense(BaseModel):
    date: Optional[date] = None
    amount: int
    Destination: str

class FinanceUpdateExpense(FinanceCreateExpense):
    amount: int
    Destination: str

class FinanceResponseExpense(FinanceCreateExpense):
    id: int
    date: date
    model_config = ConfigDict(from_attributes=True)