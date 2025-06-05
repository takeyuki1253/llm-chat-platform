from sqlalchemy import Column, String, Text, ForeignKey, JSON, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.config.database import Base
from src.models.base import BaseModel


class ChatSession(Base, BaseModel):
    __tablename__ = "chat_sessions"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    tags = Column(ARRAY(String), default=[])
    
    # Relationships
    user = relationship("User", back_populates="chat_sessions")
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")


class Message(Base, BaseModel):
    __tablename__ = "messages"
    
    session_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.id"), nullable=False)
    content = Column(Text, nullable=False)
    type = Column(String(20), nullable=False)  # 'user' or 'assistant'
    
    # Store LLM responses as JSON
    responses = Column(JSON, default=[])
    
    # Relationships
    session = relationship("ChatSession", back_populates="messages")
    evaluations = relationship("Evaluation", back_populates="message", cascade="all, delete-orphan")