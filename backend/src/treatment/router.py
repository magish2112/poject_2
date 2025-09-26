from fastapi import APIRouter, Depends, HTTPException
from src.treatment.schemas import TreatmentPlanBase, TreatmentPlanCreate
from src.treatment.service import (
    get_treatment_plan_by_id,
    get_treatment_plans_for_patient,
    create_treatment_plan,
    update_treatment_plan,
    delete_treatment_plan,
    create_patient_report,
    get_patient_reports,
    create_purchase,
    get_purchase_history
)
from src.models.report import PatientReportCreate, PatientReportResponse
from src.models.purchase import PurchaseCreate, PurchaseResponse
from src.auth.dependencies import get_current_user
from typing import List
from sqlmodel import Session
from src.database import get_session
from src.models.treatment import TreatmentPlan

router = APIRouter(prefix="/treatment", tags=["treatment"])

@router.get("/patient/{patient_id}", response_model=List[TreatmentPlanBase])
def get_patient_treatment_plans(patient_id: int, current_user=Depends(get_current_user)):
    return get_treatment_plans_for_patient(patient_id)

@router.get("/{plan_id}", response_model=TreatmentPlanBase)
def get_plan(plan_id: int, current_user=Depends(get_current_user)):
    return get_treatment_plan_by_id(plan_id)

@router.post("/", response_model=TreatmentPlanBase)
def create_plan(data: TreatmentPlanCreate, current_user=Depends(get_current_user)):
    return create_treatment_plan(data)

@router.patch("/{plan_id}", response_model=TreatmentPlanBase)
def update_plan(plan_id: int, data: TreatmentPlanCreate, current_user=Depends(get_current_user)):
    return update_treatment_plan(plan_id, data)

@router.delete("/{plan_id}")
def delete_plan(plan_id: int, current_user=Depends(get_current_user)):
    delete_treatment_plan(plan_id)
    return {"ok": True}

# --- Patient Reports ---
@router.post("/patient/{patient_id}/report", response_model=PatientReportResponse)
def create_report(patient_id: int, data: PatientReportCreate, current_user=Depends(get_current_user)):
    return create_patient_report(patient_id, data)

@router.get("/patient/{patient_id}/reports", response_model=List[PatientReportResponse])
def get_reports(patient_id: int, current_user=Depends(get_current_user)):
    return get_patient_reports(patient_id)

# --- Purchases ---
@router.post("/patient/{patient_id}/purchase", response_model=PurchaseResponse)
def create_purchase_route(patient_id: int, data: PurchaseCreate, current_user=Depends(get_current_user)):
    return create_purchase(patient_id, data)

@router.get("/patient/{patient_id}/purchases", response_model=List[PurchaseResponse])
def get_purchase_history_route(patient_id: int, current_user=Depends(get_current_user)):
    return get_purchase_history(patient_id)

@router.post("/plans", response_model=TreatmentPlan)
def create_plan_route(data: TreatmentPlan, session: Session = Depends(get_session)):
    session.add(data)
    session.commit()
    session.refresh(data)
    return data
