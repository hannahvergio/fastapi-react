from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Task, Base
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend domain here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Models
class TaskCreate(BaseModel):
    text: str
    completed: bool = False

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# Routes
@app.get("/tasks/", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.post("/tasks/", response_model=TaskOut)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/tasks/{task_id}/", response_model=TaskOut)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.text = task.text
    db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}


