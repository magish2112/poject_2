from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class PatientReport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patientprofile.id")
    treatment_plan_id: int = Field(foreign_key="treatmentplan.id")
    report_text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    patient: "PatientProfile" = Relationship(back_populates="reports")
    treatment_plan: "TreatmentPlan" = Relationship()

# Pydantic-схемы для API
from pydantic import BaseModel

class PatientReportCreate(BaseModel):
    treatment_plan_id: int
    report_text: str

class PatientReportResponse(BaseModel):
    id: int
    patient_id: int
    treatment_plan_id: int
    report_text: str
    created_at: datetime 