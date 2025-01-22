from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(120), nullable=False, unique=True)
    user_role = Column(String(50), nullable=True)

    # 定义与 WorkLog 的关系
    work_logs = relationship("WorkLog", back_populates="user")
