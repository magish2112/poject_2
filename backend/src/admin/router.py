from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from src.database import get_session
from .dependencies import get_current_admin
from .service import get_all_users, update_user_role, delete_user
from .schemas import UserOut

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=list[UserOut])
def list_users(admin=Depends(get_current_admin), session: Session = Depends(get_session)):
    return get_all_users(session)

@router.patch("/users/{user_id}/role", response_model=UserOut)
def change_role(user_id: int, role: str = Query(...), admin=Depends(get_current_admin), session: Session = Depends(get_session)):
    user = update_user_role(user_id, role, session)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@router.delete("/users/{user_id}")
def remove_user(user_id: int, admin=Depends(get_current_admin), session: Session = Depends(get_session)):
    ok = delete_user(user_id, session)
    if not ok:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"ok": True}
