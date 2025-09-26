from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Plan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    patient_id: int
    doctor_id: int
    date: datetime
