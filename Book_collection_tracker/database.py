from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_LOCALHOST = os.getenv("DB_LOCALHOST")
DB_PORT = os.getenv("DB_PORT")

url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_LOCALHOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(url)
SessionLocal = sessionmaker(bind= engine, autoflush= False, autocommit= False)
Base = declarative_base()

def try_connection():
    try:
        with engine.connect() as connn:
            print("Databsase connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")