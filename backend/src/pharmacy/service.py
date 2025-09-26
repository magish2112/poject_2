from src.pharmacy.schemas import PharmacyProduct, PharmacyOrderRequest, PharmacyOrderResponse, PharmacyOrderStatusResponse
from typing import List

# Здесь должны быть реальные вызовы к внешнему API аптеки
# Пока реализуем как заглушки

def get_pharmacy_products() -> List[PharmacyProduct]:
    # Пример заглушки
    return [
        PharmacyProduct(id="ext1", name="Витамин D", description="Иммунитет", price=500),
        PharmacyProduct(id="ext2", name="Омега-3", description="Пищ. добавка", price=900)
    ]

def create_pharmacy_order(order: PharmacyOrderRequest) -> PharmacyOrderResponse:
    # Пример заглушки
    return PharmacyOrderResponse(order_id="order123", status="created", price=1000, discount=100)

def get_order_status(order_id: str) -> PharmacyOrderStatusResponse:
    # Пример заглушки
    return PharmacyOrderStatusResponse(order_id=order_id, status="delivered", delivered=True)

def get_medications():
    # Возвращаем список фейковых лекарств
    return [
        {"id": 1, "name": "Парацетамол", "price": 100},
        {"id": 2, "name": "Ибупрофен", "price": 150},
    ]
