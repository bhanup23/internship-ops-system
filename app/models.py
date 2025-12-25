from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)

class Intern(Base):
    __tablename__ = "interns"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)
    intern_id = Column(Integer, ForeignKey("interns.id"))
