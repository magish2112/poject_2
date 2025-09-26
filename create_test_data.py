import sys
import os
sys.path.append('backend')

from sqlmodel import Session
from backend.src.database import engine
from backend.src.models.user import User, DoctorProfile, PatientProfile
from backend.src.models.medication import Medication
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_test_data():
    # Создаем таблицы
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        # Проверяем, есть ли уже пользователи
        existing_doctor = session.exec(select(User).where(User.email == "doctor@example.com")).first()
        if existing_doctor:
            print("Тестовые данные уже существуют!")
            return
            
        # Врач
        doctor_user = User(
            email="doctor@example.com", 
            hashed_password=get_password_hash("password123"), 
            role="doctor",
            first_name="Иван",
            last_name="Иванов"
        )
        session.add(doctor_user)
        session.commit()
        session.refresh(doctor_user)
        
        doctor_profile = DoctorProfile(
            user_id=doctor_user.id, 
            first_name="Иван", 
            last_name="Иванов", 
            specialization="Терапевт",
            phone="+7-999-123-45-67"
        )
        session.add(doctor_profile)

        # Пациент
        patient_user = User(
            email="patient@example.com", 
            hashed_password=get_password_hash("password123"), 
            role="patient",
            first_name="Петр",
            last_name="Петров"
        )
        session.add(patient_user)
        session.commit()
        session.refresh(patient_user)
        
        patient_profile = PatientProfile(
            user_id=patient_user.id, 
            first_name="Петр", 
            last_name="Петров",
            phone="+7-999-765-43-21"
        )
        session.add(patient_profile)

        # Препарат
        med = Medication(
            name="Витамин D3", 
            description="Поддержка иммунитета и костной системы", 
            external_id="ext123",
            price=1500.0
        )
        session.add(med)

        session.commit()
        print("✅ Тестовые данные успешно созданы!")
        print("\n🔑 Данные для входа:")
        print("👨‍⚕️ Врач:")
        print("   Email: doctor@example.com")
        print("   Пароль: password123")
        print("\n👤 Пациент:")
        print("   Email: patient@example.com") 
        print("   Пароль: password123")

if __name__ == "__main__":
    from sqlmodel import select
    create_test_data()
