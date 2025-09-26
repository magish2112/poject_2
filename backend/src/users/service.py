from src.models.user import User
from src.database import engine
from sqlmodel import Session, select
from fastapi import HTTPException

# Заглушки вместо работы с БД
def get_user_by_id(user_id: int, session: Session):
    return session.get(User, user_id)

def get_all_users(session: Session):
    return session.exec(select(User)).all()

def create_user(user_data):
    # Просто возвращаем то, что пришло, с фейковым id
    return {"id": 3, **user_data}

def update_user(user_id: int, data):
    # Возвращаем фейковые данные
    return {
        "id": user_id,
        "email": f"user{user_id}@example.com",
        "role": "user",
        "first_name": data.first_name or "Имя",
        "last_name": data.last_name or "Фамилия",
        "phone": data.phone or "1234567890"
    }

def get_users_by_role(role: str):
    users = get_all_users()
    return [u for u in users if u["role"] == role]
