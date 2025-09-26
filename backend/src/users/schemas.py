from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    id: int
    email: EmailStr
    role: str
    first_name: str
    last_name: str
    phone: Optional[str] = None

class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    specialization: Optional[str] = None  # для врача
    date_of_birth: Optional[str] = None   # для пациента

class UserListResponse(BaseModel):
    users: list[UserBase]

class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: str
    first_name: str
    last_name: str
