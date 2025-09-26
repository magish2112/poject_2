from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PrescriptionBase(BaseModel):
    id: int
    medication_id: int
    dosage: str
    frequency: str
    duration: str
    notes: Optional[str] = None

class PrescriptionCreate(BaseModel):
    medication_id: int
    dosage: str
    frequency: str
    duration: str
    notes: Optional[str] = None

class TreatmentPlanBase(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool
    prescriptions: List[PrescriptionBase] = []

class TreatmentPlanCreate(BaseModel):
    doctor_id: int
    patient_id: int
    title: str
    description: Optional[str] = None
    prescriptions: List[PrescriptionCreate] = []
