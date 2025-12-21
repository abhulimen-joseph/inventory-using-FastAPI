from sqlalchemy import Column, Integer, String, Enum, Text
from database import Base
import enum

class BookCondition(enum.Enum):
    NEW = "new"
    GOOD = "good"
    OLD = "old"
    POOR = "poor"

class ReadStatus(enum.Enum):
    STARTED = "started"
    FINISHED = "finished"
    ABANDONED = "abandoned"
    INPROGRESS= "in_progress"


class BookModel(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key= True, index=True)
    title = Column(String(200), nullable= False)
    author = Column(String(200), nullable= False)
    year = Column(int(10))
    genre = Column(String(200))
    condition = Column(Enum(BookCondition), default=BookCondition.GOOD)
    read_status = Column(Enum(ReadStatus), default=ReadStatus.STARTED)
    rating = Column(Integer)
    notes = Column(Text)

    def __repl__(self):
        print(f"<{self.title}> by <{self.author}> in <{self.condition.value}> condition")