from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Expense(Base):
    __tablename__ = "expenses"