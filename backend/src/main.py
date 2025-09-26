from fastapi import FastAPI
from sqlmodel import SQLModel
from src.database import engine
from src.auth.router import router as auth_router
from src.users.router import router as users_router
from sqladmin import Admin, ModelView
from src.models.user import User, DoctorProfile, PatientProfile
from src.models.treatment import TreatmentPlan, Prescription
from src.models.medication import Medication
from src.models.purchase import Purchase
from src.models.report import PatientReport
from fastapi.middleware.cors import CORSMiddleware
from src.patients.router import router as patients_router
from src.treatment.router import router as treatment_router
from src.admin.router import router as admin_router
from src.pharmacy.router import router as pharmacy_router
from src.plan.router import router as plan_router
from src.medication.router import router as medication_router

app = FastAPI(title="Fullscript Analog Backend")

# Добавь это ДО include_router!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # или ["*"] для всех
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Автоматическое создание таблиц (для разработки)
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(patients_router)
app.include_router(treatment_router)
app.include_router(admin_router)
app.include_router(pharmacy_router)
app.include_router(plan_router)  # Added plans endpoint
app.include_router(medication_router)

# Создаём админ-панель
admin = Admin(app, engine)

# Регистрируем модели для админки
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.role, User.created_at, User.updated_at]
    name = "Пользователь"
    name_plural = "Пользователи"
    column_labels = {
        "id": "ID",
        "email": "Email",
        "role": "Роль",
        "created_at": "Создан",
        "updated_at": "Обновлён"
    }

class DoctorProfileAdmin(ModelView, model=DoctorProfile):
    column_list = [DoctorProfile.id, DoctorProfile.user_id, DoctorProfile.first_name, DoctorProfile.last_name, DoctorProfile.specialization]
    name = "Профиль врача"
    name_plural = "Профили врачей"
    column_labels = {
        "id": "ID",
        "user_id": "Пользователь",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "specialization": "Специализация"
    }

class PatientProfileAdmin(ModelView, model=PatientProfile):
    column_list = [PatientProfile.id, PatientProfile.user_id, PatientProfile.first_name, PatientProfile.last_name, PatientProfile.date_of_birth]
    name = "Профиль пациента"
    name_plural = "Профили пациентов"
    column_labels = {
        "id": "ID",
        "user_id": "Пользователь",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "date_of_birth": "Дата рождения"
    }

class TreatmentPlanAdmin(ModelView, model=TreatmentPlan):
    column_list = [TreatmentPlan.id, TreatmentPlan.doctor_id, TreatmentPlan.patient_id, TreatmentPlan.title]
    name = "Курс лечения"
    name_plural = "Курсы лечения"
    column_labels = {
        "id": "ID",
        "doctor_id": "Врач",
        "patient_id": "Пациент",
        "title": "Название"
    }

class PrescriptionAdmin(ModelView, model=Prescription):
    column_list = [Prescription.id, Prescription.treatment_plan_id, Prescription.medication_id, Prescription.dosage]
    name = "Назначение"
    name_plural = "Назначения"
    column_labels = {
        "id": "ID",
        "treatment_plan_id": "Курс лечения",
        "medication_id": "Препарат",
        "dosage": "Дозировка"
    }

class MedicationAdmin(ModelView, model=Medication):
    column_list = [
        Medication.id,
        Medication.name,
        Medication.brand,
        Medication.form,
        Medication.price,
        Medication.external_id,
        # Medication.prescriptions  # Не добавляйте связи, если не требуется!
    ]
    name = "Препарат"
    name_plural = "Препараты"
    column_labels = {
        "id": "ID",
        "name": "Название",
        "brand": "Бренд",
        "form": "Форма выпуска",
        "price": "Цена",
        "external_id": "Внешний ID"
        # Не добавляйте prescriptions!
    }

class PurchaseAdmin(ModelView, model=Purchase):
    column_list = [Purchase.id, Purchase.patient_id, Purchase.prescription_id, Purchase.status, Purchase.price]
    name = "Покупка"
    name_plural = "Покупки"
    column_labels = {
        "id": "ID",
        "patient_id": "Пациент",
        "prescription_id": "Назначение",
        "status": "Статус",
        "price": "Цена"
    }

class PatientReportAdmin(ModelView, model=PatientReport):
    column_list = [PatientReport.id, PatientReport.patient_id, PatientReport.treatment_plan_id, PatientReport.report_text]
    name = "Отчёт пациента"
    name_plural = "Отчёты пациентов"
    column_labels = {
        "id": "ID",
        "patient_id": "Пациент",
        "treatment_plan_id": "Курс лечения",
        "report_text": "Текст отчёта"
    }

admin.add_view(UserAdmin)
admin.add_view(DoctorProfileAdmin)
admin.add_view(PatientProfileAdmin)
admin.add_view(TreatmentPlanAdmin)
admin.add_view(PrescriptionAdmin)
admin.add_view(MedicationAdmin)
admin.add_view(PurchaseAdmin)
admin.add_view(PatientReportAdmin)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
