# Backend (FastAPI + SQLModel)

## Структура проекта
src/
│
├── database.py # Подключение к базе данных и сессии
├── models/ # Все модели данных (ORM)
│ ├── init.py
│ ├── user.py # User, DoctorProfile, PatientProfile
│ ├── treatment.py # TreatmentPlan, Prescription
│ ├── medication.py # Medication
│ ├── purchase.py # Purchase
│ └── report.py # PatientReport
├── main.py               # Точка входа FastAPI
├── migrations/           # Миграции Alembic
│   ├── env.py
│   └── versions/
├── alembic.ini           # Конфиг Alembic

## Описание моделей

- **User** — базовый пользователь (роль: врач, пациент, админ)
- **DoctorProfile** — профиль врача
- **PatientProfile** — профиль пациента
- **TreatmentPlan** — курс лечения (связь врач-пациент)
- **Prescription** — назначение в рамках курса
- **Medication** — справочник препаратов
- **Purchase** — покупка препарата пациентом
- **PatientReport** — отчет пациента по курсу

## Подключение к базе данных

В файле `src/database.py`:
- Используется SQLModel и SQLAlchemy engine.
- Строка подключения берется из переменной окружения `DATABASE_URL`.

## Миграции

Для миграций используется Alembic.  
Инструкции по настройке — см. ниже.

## Быстрый старт

1. Установи зависимости:
   ```
   pip install fastapi sqlmodel alembic psycopg2-binary uvicorn
   ```
2. Настрой переменную окружения `DATABASE_URL` или измени строку в `alembic.ini`.
3. Инициализируй и примени миграции:
   ```
   cd src
   alembic revision --autogenerate -m "Initial tables"
   alembic upgrade head
   ```
4. Запусти сервер:
   ```
   uvicorn src.main:app --reload
   ```

