# app/models/todo.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from app.database.base_class import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    #待做的工作标题，
    task_name = Column(
        String(120),
        index=True,
    )
    # 工作描述
    description = Column(String(255), index=True, nullable=True)
    #ddl
    due_date = Column(DateTime, index=True, nullable=True)
    # 预计工时
    estimated_hours = Column(Integer, index=True)
    # 实际工时
    actual_hours = Column(Integer, index=True)
    is_completed = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # 添加与 WorkLog 的关系
    #work_logs = relationship("WorkLog", back_populates="task")  # 定义关系
    #根据需求写了点，没有测试

    def __str__(self):
        return f"Todo job #{self.id}: {self.title}, Estimated Hours: {self.estimated_hours}, Actual Hours: {self.actual_hours}, Completed: {self.is_completed}"
