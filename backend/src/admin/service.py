from src.models.user import User
from sqlmodel import Session, select

def get_all_users(session: Session):
    return session.exec(select(User)).all()

def update_user_role(user_id: int, role: str, session: Session):
    user = session.get(User, user_id)
    if not user:
        return None
    user.role = role
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True
