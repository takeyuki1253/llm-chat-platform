from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.config.database import Base
from src.models.base import BaseModel


class Evaluation(Base, BaseModel):
    __tablename__ = "evaluations"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    message_id = Column(UUID(as_uuid=True), ForeignKey("messages.id"), nullable=False)
    provider = Column(String(50), nullable=False)
    
    # Ratings
    usefulness_rating = Column(Integer, nullable=True)
    accuracy_rating = Column(Integer, nullable=True)
    creativity_rating = Column(Integer, nullable=True)
    
    # Feedback
    feedback = Column(Text, nullable=True)
    
    # Auto-evaluation metrics
    auto_metrics = Column(JSON, default={})
    
    # Relationships
    user = relationship("User", back_populates="evaluations")
    message = relationship("Message", back_populates="evaluations")