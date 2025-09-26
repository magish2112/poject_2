from fastapi import APIRouter, Depends, HTTPException, status
from src.auth.schemas import UserRegisterRequest, UserLoginRequest, TokenResponse, UserResponse
from src.auth.service import get_password_hash, authenticate_user, create_access_token
from src.auth.dependencies import get_current_user
from sqlmodel import Session, select
from src.database import get_session
from src.models.user import User, DoctorProfile, PatientProfile

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(data: UserRegisterRequest, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.email == data.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(data.password)
    user = User(
        email=data.email,
        hashed_password=hashed_password,
        role=data.role,
        first_name=data.first_name,
        last_name=data.last_name
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    # Создаём профиль врача или пациента
    if data.role == "doctor":
        doctor_profile = DoctorProfile(
            user_id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            specialization=data.specialization,
            phone=data.phone
        )
        session.add(doctor_profile)
    elif data.role == "patient":
        patient_profile = PatientProfile(
            user_id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            phone=data.phone
        )
        session.add(patient_profile)
    session.commit()

    return UserResponse(
        id=user.id,
        email=user.email,
        role=user.role,
        first_name=user.first_name,
        last_name=user.last_name
    )

@router.post("/login", response_model=TokenResponse)
def login(data: UserLoginRequest, session: Session = Depends(get_session)):
    user = authenticate_user(data.email, data.password, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token = create_access_token({"sub": user.email, "role": user.role})
    return TokenResponse(access_token=token)

@router.get("/me", response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        role=current_user.role,
        first_name=current_user.first_name,
        last_name=current_user.last_name
    )
