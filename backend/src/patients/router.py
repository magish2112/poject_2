from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from src.database import get_session
from src.models.patient import Patient

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=Patient)
def create_patient(data: Patient, session: Session = Depends(get_session)):
    session.add(data)
    session.commit()
    session.refresh(data)
    return data

@router.get("/", response_model=list[Patient])
def list_patients(session: Session = Depends(get_session)):
    return session.exec(select(Patient)).all()

@router.get("/search/", response_model=list[Patient])
def search_patients(q: str = Query(..., min_length=1), session: Session = Depends(get_session)):
    # Поиск по имени или фамилии (регистр не важен)
    return session.exec(
        select(Patient).where(
            (Patient.first_name.ilike(f"%{q}%")) | (Patient.last_name.ilike(f"%{q}%"))
        )
    ).all()
