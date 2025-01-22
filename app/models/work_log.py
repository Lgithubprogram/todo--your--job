from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class WorkLog(Base):
    __tablename__ = "work_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("todos.id"), nullable=False)  # 外键关联到 Task 表
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # 外键关联到 User 表
    hours_spent = Column(Integer, nullable=False)  # 花费的工时
    work_date = Column(DateTime, nullable=False)  # 记录日期
    log_type = Column(String(50), nullable=True)  # 工时记录类型（如计划、实际）

    # 定义与 Task 和 User 的反向关系
    task = relationship("Todo", back_populates="work_logs")
    user = relationship("User", back_populates="work_logs")
