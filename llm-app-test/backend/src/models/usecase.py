from sqlalchemy import Column, String, Text, Boolean, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.config.database import Base
from src.models.base import BaseModel


class UseCase(Base, BaseModel):
    __tablename__ = "use_cases"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    prompt_template = Column(Text, nullable=False)
    expected_output = Column(Text, nullable=True)
    evaluation_criteria = Column(JSON, default={})
    schedule = Column(String(100), nullable=True)  # Cron expression
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Execution history
    execution_history = Column(JSON, default=[])
    
    # Relationships
    user = relationship("User", back_populates="use_cases")