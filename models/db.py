from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True)
    name = Column(String, unique=True)
    username = Column(String)
    password = Column(String)
    budget = Column(Integer)

engine = create_engine("sqlite:///expense_tracker.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)