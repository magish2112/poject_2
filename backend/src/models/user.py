from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    role: str  # 'doctor', 'patient', 'admin'
    first_name: str
    last_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    doctor_profile: Optional["DoctorProfile"] = Relationship(back_populates="user")
    patient_profile: Optional["PatientProfile"] = Relationship(back_populates="user")

class DoctorProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    first_name: str
    last_name: str
    specialization: Optional[str]
    phone: Optional[str]

    user: User = Relationship(back_populates="doctor_profile")
    treatment_plans: list["TreatmentPlan"] = Relationship(back_populates="doctor")

class PatientProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    first_name: str
    last_name: str
    date_of_birth: Optional[datetime]
    phone: Optional[str]

    user: User = Relationship(back_populates="patient_profile")
    treatment_plans: list["TreatmentPlan"] = Relationship(back_populates="patient")
    purchases: list["Purchase"] = Relationship(back_populates="patient")
    reports: list["PatientReport"] = Relationship(back_populates="patient") 