from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_LOCALHOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_LOCALHOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL)
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind= engine)
Base = declarative_base()

def test_connection():
    try:
        with engine.connect() as conn:
            print("Database connection susccessful")
    except Exception as e:
        print(f"Database connection failed: {e}")