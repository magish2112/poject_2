import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from sqlmodel import Session
from backend.src.database import engine
from backend.src.models.user import User, DoctorProfile, PatientProfile
from backend.src.models.medication import Medication
from backend.src.auth.service import get_password_hash

def seed():
    with Session(engine) as session:
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
        doctor_profile = DoctorProfile(
            user_id=doctor_user.id, 
            first_name="Иван", 
            last_name="Иванов", 
            specialization="Терапевт"
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
        patient_profile = PatientProfile(
            user_id=patient_user.id, 
            first_name="Петр", 
            last_name="Петров"
        )
        session.add(patient_profile)

        # Препарат
        med = Medication(name="Витамин D", description="Иммунитет", external_id="ext123")
        session.add(med)

        session.commit()
        print("Демо-данные успешно добавлены!")

if __name__ == "__main__":
    seed()
