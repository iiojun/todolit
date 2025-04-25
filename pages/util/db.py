from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Date, Boolean

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todo'
    todo_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    deadline = Column(Date)
    done = Column(Boolean)

def create_db_connection():
    # DB settings
    engine = create_engine('sqlite:///db.sqlite3')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

session, engine = create_db_connection()
Base.metadata.create_all(engine)

