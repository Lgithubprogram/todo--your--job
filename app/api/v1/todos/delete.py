# app/api/v1/todos/delete.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.todo import Todo

router = APIRouter()


@router.delete("/todos/{id}")
async def delete_todo(id: int, db: Session = Depends(get_db)):
    """
    Delete a todojob.
    """
    db_todo = db.query(Todo).filter(Todo.id == id).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()

    return {"message": "Todojob  deleted successfully"}
