# app/api/v1/todos/create.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.todo import TodoCreate
from app.schemas.todo import Todo as TodoResponse
from app.models.todo import Todo
from datetime import datetime

router = APIRouter()


@router.post("/todos/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new todo.
    """
    # You can customize this logic based on your requirements.
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        is_completed=todo.is_completed,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
