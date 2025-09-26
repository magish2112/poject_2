from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.database import get_session
from src.models.plan import Plan
from datetime import datetime

router = APIRouter(prefix="/plans", tags=["plans"])

@router.get("/", response_model=list[Plan])
def list_plans(session: Session = Depends(get_session)):
    plans = session.exec(select(Plan)).all()
    return plans

@router.post("/", response_model=Plan)
def create_plan(plan: Plan, session: Session = Depends(get_session)):
    # Set default date if not provided
    if not plan.date:
        plan.date = datetime.utcnow()
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan

@router.put("/{plan_id}", response_model=Plan)
def update_plan(plan_id: int, plan_data: Plan, session: Session = Depends(get_session)):
    plan = session.get(Plan, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    for key, value in plan_data.dict(exclude_unset=True).items():
        setattr(plan, key, value)
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan

@router.delete("/{plan_id}")
def delete_plan(plan_id: int, session: Session = Depends(get_session)):
    plan = session.get(Plan, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    session.delete(plan)
    session.commit()
    return {"ok": True}