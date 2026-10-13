from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.utils.db import Base

class TaskModal(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    desc = Column(String(1080), nullable=True)
    is_complete = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"))