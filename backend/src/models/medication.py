from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Medication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    brand: Optional[str] = None
    form: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    external_id: Optional[str] = None  # id препарата во внешней аптеке

    prescriptions: list["Prescription"] = Relationship(back_populates="medication")