from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Purchase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patientprofile.id")
    prescription_id: int = Field(foreign_key="prescription.id")
    external_order_id: Optional[str]
    status: str  # created/paid/delivered/...
    price: Optional[float]
    discount: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    patient: "PatientProfile" = Relationship(back_populates="purchases")
    prescription: "Prescription" = Relationship(back_populates="purchases")

# Pydantic-схемы для API
from pydantic import BaseModel

class PurchaseCreate(BaseModel):
    prescription_id: int
    external_order_id: Optional[str] = None
    status: str = "created"
    price: Optional[float] = None
    discount: Optional[float] = None

class PurchaseResponse(BaseModel):
    id: int
    patient_id: int
    prescription_id: int
    external_order_id: Optional[str]
    status: str
    price: Optional[float]
    discount: Optional[float]
    created_at: datetime 