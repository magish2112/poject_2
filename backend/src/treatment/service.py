from src.models import TreatmentPlan, Prescription, PatientReport
from src.database import engine
from sqlmodel import Session, select
from fastapi import HTTPException
from typing import List

def get_treatment_plan_by_id(plan_id: int):
    with Session(engine) as session:
        plan = session.get(TreatmentPlan, plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Курс лечения не найден")
        return plan

def get_treatment_plans_for_patient(patient_id: int) -> List[TreatmentPlan]:
    with Session(engine) as session:
        plans = session.exec(select(TreatmentPlan).where(TreatmentPlan.patient_id == patient_id)).all()
        return plans

def create_treatment_plan(data):
    with Session(engine) as session:
        plan = TreatmentPlan(
            doctor_id=data.doctor_id,
            patient_id=data.patient_id,
            title=data.title,
            description=data.description,
            is_active=True
        )
        session.add(plan)
        session.commit()
        session.refresh(plan)
        for presc in data.prescriptions:
            prescription = Prescription(
                treatment_plan_id=plan.id,
                medication_id=presc.medication_id,
                dosage=presc.dosage,
                frequency=presc.frequency,
                duration=presc.duration,
                notes=presc.notes
            )
            session.add(prescription)
        session.commit()
        return plan

def update_treatment_plan(plan_id: int, data):
    with Session(engine) as session:
        plan = session.get(TreatmentPlan, plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Курс лечения не найден")
        if data.title:
            plan.title = data.title
        if data.description:
            plan.description = data.description
        if data.is_active is not None:
            plan.is_active = data.is_active
        session.add(plan)
        session.commit()
        return plan

def delete_treatment_plan(plan_id: int):
    with Session(engine) as session:
        plan = session.get(TreatmentPlan, plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Курс лечения не найден")
        session.delete(plan)
        session.commit()

def create_patient_report(patient_id: int, data):
    with Session(engine) as session:
        report = PatientReport(
            patient_id=patient_id,
            treatment_plan_id=data.treatment_plan_id,
            report_text=data.report_text
        )
        session.add(report)
        session.commit()
        session.refresh(report)
        return report

def get_patient_reports(patient_id: int):
    with Session(engine) as session:
        reports = session.exec(select(PatientReport).where(PatientReport.patient_id == patient_id)).all()
        return reports

def create_purchase(patient_id: int, data):
    # Возвращаем фейковую покупку
    return {
        "id": 1,
        "patient_id": patient_id,
        "medication": data.get("medication", "TestMed"),
        "amount": data.get("amount", 1),
        "status": "created"
    }

def get_purchase_history(patient_id: int):
    # Возвращаем список фейковых покупок
    return [
        {"id": 1, "patient_id": patient_id, "medication": "TestMed", "amount": 1, "status": "created"},
        {"id": 2, "patient_id": patient_id, "medication": "TestMed2", "amount": 2, "status": "completed"},
    ]
