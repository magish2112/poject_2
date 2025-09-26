from pydantic import BaseModel
from typing import Optional, List

class PharmacyProduct(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: Optional[float] = None

class PharmacyOrderRequest(BaseModel):
    patient_id: int
    prescription_id: int
    quantity: int

class PharmacyOrderResponse(BaseModel):
    order_id: str
    status: str
    price: float
    discount: Optional[float] = None

class PharmacyOrderStatusResponse(BaseModel):
    order_id: str
    status: str
    delivered: bool

class UserBase(BaseModel):
    # ...
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "user@example.com",
                "role": "doctor",
                "first_name": "Иван",
                "last_name": "Иванов",
                "phone": "+79991234567"
            }
        }
