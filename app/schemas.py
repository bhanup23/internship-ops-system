from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class InternCreate(BaseModel):
    name: str
    department: str

class TaskCreate(BaseModel):
    title: str
    intern_id: int
