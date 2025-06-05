from typing import Optional, Dict, Any, List
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    name: str
    is_active: bool = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    id: UUID
    hashed_password: str
    is_superuser: bool
    api_keys: Dict[str, Any] = {}
    settings: Dict[str, Any] = {}
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class User(UserBase):
    id: UUID
    is_superuser: bool
    api_keys: Dict[str, Any] = {}
    settings: Dict[str, Any] = {}
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenResponse(BaseModel):
    token: str
    user: User


class ApiKeysUpdate(BaseModel):
    openai: Optional[str] = None
    google: Optional[str] = None
    google_models: Optional[List[str]] = None
    anthropic: Optional[str] = None


class PasswordChange(BaseModel):
    current_password: str
    new_password: str
