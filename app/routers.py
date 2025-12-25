from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User, Intern, Task
from app.schemas import UserCreate, InternCreate, TaskCreate
from app.auth import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/intern")
def add_intern(intern: InternCreate, db: Session = Depends(get_db)):
    db.add(Intern(**intern.dict()))
    db.commit()
    return {"msg": "Intern added"}

@router.post("/task")
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    db.add(Task(title=task.title, status="pending", intern_id=task.intern_id))
    db.commit()
    return {"msg": "Task assigned"}
