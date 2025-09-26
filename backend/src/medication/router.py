from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.database import get_session
from src.models.medication import Medication

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/", response_model=list[Medication])
def list_catalog(session: Session = Depends(get_session)):
    return session.exec(select(Medication)).all()

@router.post("/", response_model=Medication)
def add_product(med: Medication, session: Session = Depends(get_session)):
    session.add(med)
    session.commit()
    session.refresh(med)
    return med

@router.get("/{med_id}", response_model=Medication)
def get_product(med_id: int, session: Session = Depends(get_session)):
    med = session.get(Medication, med_id)
    if not med:
        raise HTTPException(status_code=404, detail="Product not found")
    return med

@router.delete("/{med_id}")
def delete_product(med_id: int, session: Session = Depends(get_session)):
    med = session.get(Medication, med_id)
    if not med:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(med)
    session.commit()
    return {"ok": True}
