from sqlalchemy import Column, Integer, String, Float, Enum, Date
from sqlalchemy.sql import func
from database import Base
import enum



class Frequency(enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class VariableExpense(enum.Enum):
    FOOD = 'food'
    SNACKS = "snacks"
    ENTERTAINMENT = "entertainment"
    ONLINE_PURCHASE = "online purchase"

class FixedExpenses(enum.Enum):
    RENT = "rent"
    TRANPORT = "transport"
    SUBSCRIPTION = "subscription"
    UTILITIES = "utilities"

class Income(Base):
    __tablename__ = "Income"
    
    id = Column(Integer, primary_key=True, index = True)
    date = Column(Date, nullable = False, server_default=func.current_date())
    amount = Column(Float, nullable= False)
    source = Column(String, nullable= False)
    frequency = Column(Enum(Frequency), default = Frequency.MONTHLY)

class Expenses(Base):
    __tablename__ = "Expenses"
    id = Column(Integer, primary_key = True, index = True)
    date = Column(Date, nullable = False, server_default = func.current_date())
    amount = Column(Float, nullable= False)
    Destination = Column(String, nullable= False)

# class Savings(Income, Expenses):
#     __tablename__ = "Savings"
#     id = Column(Integer)
#     savings = Column


# class Debts(Base):
#     __tablename__ = "Debts"

# class BalanceCheck(Base):
#     __tablename__ = "BalanceCheck"

