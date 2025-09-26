from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class TreatmentPlan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: int = Field(foreign_key="doctorprofile.id")
    patient_id: int = Field(foreign_key="patientprofile.id")
    title: str
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    doctor: "DoctorProfile" = Relationship(back_populates="treatment_plans")
    patient: "PatientProfile" = Relationship(back_populates="treatment_plans")
    prescriptions: list["Prescription"] = Relationship(back_populates="treatment_plan")

class Prescription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    treatment_plan_id: int = Field(foreign_key="treatmentplan.id")
    medication_id: int = Field(foreign_key="medication.id")
    dosage: str
    frequency: str
    duration: str
    notes: Optional[str]

    treatment_plan: TreatmentPlan = Relationship(back_populates="prescriptions")
    medication: "Medication" = Relationship(back_populates="prescriptions")
    purchases: list["Purchase"] = Relationship(back_populates="prescription") 