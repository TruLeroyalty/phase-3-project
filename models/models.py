from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Integer)
    user_id = Column(Integer,ForeignKey("users.id"))

    user = relationship("User", back_populates="expenses")