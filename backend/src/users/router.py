from fastapi import APIRouter, Depends, HTTPException
from src.users.schemas import UserBase, UserUpdateRequest, UserListResponse
from src.users.service import get_user_by_id, get_all_users, update_user, get_users_by_role
from src.auth.dependencies import get_current_user
from sqlmodel import Session
from src.database import get_session
from sqlalchemy import select
from src.models.user import User, DoctorProfile, PatientProfile

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UserListResponse)
def list_users(current_user=Depends(get_current_user)):
    users = get_all_users()
    result = []
    for user in users:
        profile = user.get("doctor_profile") or user.get("patient_profile")
        result.append(UserBase(
            id=user.id,
            email=user.email,
            role=user.role,
            first_name=getattr(profile, 'first_name', None),
            last_name=getattr(profile, 'last_name', None),
            phone=getattr(profile, 'phone', None)
        ))
    return UserListResponse(users=result)

@router.get("/{user_id}", response_model=UserBase)
def get_user(user_id: int, current_user=Depends(get_current_user)):
    user = get_user_by_id(user_id)
    profile = user.get("doctor_profile") or user.get("patient_profile")
    return UserBase(
        id=user.id,
        email=user.email,
        role=user.role,
        first_name=getattr(profile, 'first_name', None),
        last_name=getattr(profile, 'last_name', None),
        phone=getattr(profile, 'phone', None)
    )

@router.patch("/{user_id}", response_model=UserBase)
def update_user_profile(user_id: int, data: UserUpdateRequest, current_user=Depends(get_current_user)):
    user = update_user(user_id, data)
    profile = user.get("doctor_profile") or user.get("patient_profile")
    return UserBase(
        id=user.id,
        email=user.email,
        role=user.role,
        first_name=getattr(profile, 'first_name', None),
        last_name=getattr(profile, 'last_name', None),
        phone=getattr(profile, 'phone', None)
    )

@router.get("/role/{role}", response_model=UserListResponse)
def list_users_by_role(role: str, current_user=Depends(get_current_user)):
    users = get_users_by_role(role)
    result = []
    for user in users:
        profile = user.get("doctor_profile") or user.get("patient_profile")
        result.append(UserBase(
            id=user.id,
            email=user.email,
            role=user.role,
            first_name=getattr(profile, 'first_name', None),
            last_name=getattr(profile, 'last_name', None),
            phone=getattr(profile, 'phone', None)
        ))
    return UserListResponse(users=result)

def get_user_by_id(user_id: int):
    return {
        "id": user_id,
        "email": f"user{user_id}@example.com",
        "role": "user",
        "doctor_profile": {"first_name": "Иван", "last_name": "Иванов", "phone": "1234567890"},
        "patient_profile": None
    }
