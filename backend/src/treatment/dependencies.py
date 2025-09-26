# Здесь можно реализовать зависимости для проверки прав доступа к курсам лечения и назначениям

from fastapi import Depends, HTTPException, status
from src.auth.dependencies import get_current_user

def is_doctor(current_user=Depends(get_current_user)):
    if current_user.role != "doctor":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется роль врача")
    return current_user

def is_patient(current_user=Depends(get_current_user)):
    if current_user.role != "patient":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется роль пациента")
    return current_user
