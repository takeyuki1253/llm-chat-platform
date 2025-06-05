from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class TimestampMixin(BaseModel):
    created_at: datetime
    updated_at: datetime


class UUIDMixin(BaseModel):
    id: UUID
