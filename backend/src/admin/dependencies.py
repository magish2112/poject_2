from fastapi import Depends, HTTPException, status
from src.auth.dependencies import get_current_user

def get_current_admin(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется роль администратора")
    return user