# app/api/v1/todos/read.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.todo import Todo
from app.schemas.todo import Todo as TodoSchema
from typing import List

router = APIRouter()


@router.get("/todos/", response_model=List[TodoSchema])
async def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todojobs = db.query(Todo).offset(skip).limit(limit).all()
    return todojobs


@router.get("/todos/{id}", response_model=TodoSchema)
async def read_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
