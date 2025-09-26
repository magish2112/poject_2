from fastapi import APIRouter, Depends
from src.pharmacy.schemas import PharmacyProduct, PharmacyOrderRequest, PharmacyOrderResponse, PharmacyOrderStatusResponse
from src.pharmacy.service import get_pharmacy_products, create_pharmacy_order, get_order_status
from src.auth.dependencies import get_current_user
from typing import List

router = APIRouter(prefix="/pharmacy", tags=["pharmacy"])

@router.get("/products", response_model=List[PharmacyProduct])
def list_products(current_user=Depends(get_current_user)):
    return get_pharmacy_products()

@router.post("/order", response_model=PharmacyOrderResponse)
def order_product(order: PharmacyOrderRequest, current_user=Depends(get_current_user)):
    return create_pharmacy_order(order)

@router.get("/order/{order_id}/status", response_model=PharmacyOrderStatusResponse)
def order_status(order_id: str, current_user=Depends(get_current_user)):
    return get_order_status(order_id)
