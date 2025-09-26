from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    role: str  # 'doctor' или 'patient'
    first_name: str
    last_name: str
    specialization: Optional[str] = None  # только для врача
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None   # только для пациента (ISO-строка)

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    first_name: str
    last_name: str

class UserCreate(BaseModel):
    email: str
    password: str
    role: str
    first_name: str
    last_name: str

class UserRead(BaseModel):
    id: int
    email: str
    role: str
    first_name: str
    last_name: str

class Token(BaseModel):
    access_token: str
    token_type: str
