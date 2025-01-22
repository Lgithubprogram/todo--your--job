from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    task_name: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    estimated_hours: int = Field(..., ge=0)
    actual_hours: int  = Field(..., ge=0)
    is_completed: Optional[bool] = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
