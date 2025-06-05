from sqlalchemy import Column, String, Boolean, JSON
from sqlalchemy.orm import relationship
from src.config.database import Base
from src.models.base import BaseModel


class User(Base, BaseModel):
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    
    # Encrypted API keys
    api_keys = Column(JSON, default={})
    
    # User settings
    settings = Column(JSON, default={})
    
    # Relationships
    chat_sessions = relationship("ChatSession", back_populates="user", cascade="all, delete-orphan")
    evaluations = relationship("Evaluation", back_populates="user", cascade="all, delete-orphan")
    use_cases = relationship("UseCase", back_populates="user", cascade="all, delete-orphan")