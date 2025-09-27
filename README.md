# 🏥 Медицинская платформа - аналог Fullscript.com

Полнофункциональная веб-платформа для врачей и пациентов с возможностью назначения курсов лечения, управления препаратами и интеграцией с аптеками.

## ✨ Возможности

### 👨‍⚕️ Для врачей:
- Регистрация и авторизация
- Управление списком пациентов
- Создание курсов лечения
- Назначение препаратов с дозировками
- Отслеживание выполнения назначений
- Корректировка курсов лечения

### 👤 Для пациентов:
- Регистрация и авторизация
- Просмотр назначений и курсов лечения
- Покупка препаратов через интеграцию с аптеками
- Получение скидок и бонусов
- Отправка отчетов врачу о приеме препаратов

### 🏪 Интеграция с аптеками:
- Получение каталога препаратов
- Оформление заказов
- Отслеживание статуса заказов

### 🔧 Администрирование:
- Управление пользователями
- Модерация контента
- Просмотр аналитики

## 🛠 Технический стек

### Backend (Python)
- **FastAPI** - высокопроизводительный веб-фреймворк
- **SQLModel** - ORM для работы с базой данных
- **SQLAlchemy** - engine для подключения к БД
- **SQLite** - встроенная база данных (для разработки)
- **JWT** - аутентификация и авторизация
- **Alembic** - миграции базы данных
- **SQLAdmin** - админ-панель

### Frontend (JavaScript)
- **React 18** - пользовательский интерфейс
- **Vite** - инструмент сборки
- **Material-UI** - компоненты интерфейса
- **React Router** - маршрутизация
- **Axios** - HTTP клиент
- **Context API** - управление состоянием

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.8+
- Node.js 16+
- Git

### 1. Клонирование репозитория
```bash
git clone https://github.com/magish2112/poject_2.git
cd poject_2
```

### 2. Установка зависимостей Backend
```bash
pip install -r requirements.txt
```

### 3. Установка зависимостей Frontend
```bash
cd frontend
npm install
```

### 4. Создание тестовых данных
```bash
python create_test_data.py
```

### 5. Запуск Backend сервера
```bash
cd backend
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Запуск Frontend сервера (в новом терминале)
```bash
cd frontend
npm run dev
```

## 🌐 Доступ к приложению

- **Frontend (основной сайт):** http://localhost:5173
- **Backend API:** http://localhost:8000
- **API документация (Swagger):** http://localhost:8000/docs
- **Админ-панель:** http://localhost:8000/admin

## 🔑 Тестовые учетные записи

### 👨‍⚕️ Врач:
- **Email:** `doctor@example.com`
- **Пароль:** `password123`
- **Имя:** Иван Иванов
- **Специализация:** Терапевт

### 👤 Пациент:
- **Email:** `patient@example.com`
- **Пароль:** `password123`
- **Имя:** Петр Петров

## 📁 Структура проекта

```
poject_2/
├── backend/                 # Backend (FastAPI)
│   ├── src/
│   │   ├── auth/           # Аутентификация
│   │   ├── models/         # Модели данных
│   │   ├── patients/       # Управление пациентами
│   │   ├── treatment/      # Курсы лечения
│   │   ├── pharmacy/       # Интеграция с аптеками
│   │   ├── medication/     # Справочник препаратов
│   │   ├── admin/          # Администрирование
│   │   ├── database.py     # Подключение к БД
│   │   └── main.py         # Точка входа API
│   └── test.db             # База данных SQLite
├── frontend/               # Frontend (React)
│   ├── src/
│   │   ├── components/     # React компоненты
│   │   ├── pages/         # Страницы приложения
│   │   ├── api/           # API клиенты
│   │   ├── context/       # Context API
│   │   └── App.jsx        # Главный компонент
│   ├── package.json
│   └── index.html
├── create_test_data.py     # Скрипт создания тестовых данных
├── requirements.txt        # Python зависимости
└── README.md              # Документация
```

## 🔧 API Эндпоинты

### Аутентификация
- `POST /auth/register` - Регистрация пользователя
- `POST /auth/login` - Вход в систему
- `GET /auth/me` - Получение данных текущего пользователя

### Пациенты
- `GET /patients/` - Список пациентов (для врачей)
- `POST /patients/` - Создание пациента
- `GET /patients/{id}` - Получение данных пациента

### Курсы лечения
- `GET /plans/` - Список курсов лечения
- `POST /plans/` - Создание курса лечения
- `PUT /plans/{id}` - Обновление курса лечения

### Препараты
- `GET /medication/` - Каталог препаратов
- `GET /medication/{id}` - Информация о препарате

### Покупки
- `POST /pharmacy/purchase` - Оформление покупки

## 📊 Модели данных

### User (Пользователь)
- `id` - уникальный идентификатор
- `email` - электронная почта
- `role` - роль (врач/пациент/админ)
- `first_name` - имя
- `last_name` - фамилия

### DoctorProfile (Профиль врача)
- `user_id` - связь с пользователем
- `specialization` - специализация
- `phone` - телефон

### PatientProfile (Профиль пациента)
- `user_id` - связь с пользователем
- `date_of_birth` - дата рождения
- `phone` - телефон

### TreatmentPlan (Курс лечения)
- `doctor_id` - врач
- `patient_id` - пациент
- `title` - название курса
- `description` - описание
- `is_active` - активен ли курс

### Prescription (Назначение)
- `treatment_plan_id` - курс лечения
- `medication_id` - препарат
- `dosage` - дозировка
- `frequency` - частота приема
- `duration` - длительность

### Medication (Препарат)
- `name` - название
- `brand` - бренд
- `form` - форма выпуска
- `price` - цена
- `description` - описание

## 🔒 Безопасность

- JWT токены для аутентификации
- Хеширование паролей (bcrypt)
- CORS настроен для frontend домена
- Ролевая модель доступа

## 🚀 Развертывание

### Локальное развертывание
```bash
# Backend
cd backend
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000

# Frontend
cd frontend
npm run build
npm run preview
```

### Production (пример с Docker)
```dockerfile
# Dockerfile для backend
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contributing

1. Fork репозиторий
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в branch (`git push origin feature/amazing-feature`)
5. Создайте Pull Request

## 📄 Лицензия

Этот проект является открытым исходным кодом.

## 📞 Контакты

**Разработчик:** [magish2112](https://github.com/magish2112)

---

⭐ **Если проект понравился, поставьте звезду на GitHub!**

