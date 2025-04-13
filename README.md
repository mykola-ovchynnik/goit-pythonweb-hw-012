# 📞 FastAPI Contacts API

A complete **Contacts Management RESTful API** built with **FastAPI**, supporting:

- 🔐 User registration, login, JWT authentication
- ✅ Email confirmation with token verification
- 🔁 Password reset via email
- 📇 Contact CRUD operations with filtering and search
- 🎂 Upcoming birthday lookup
- 📤 Avatar uploads to Cloudinary
- 🚀 Gravatar fallback for avatars
- 🧱 Redis-based caching
- ⛔ Request rate-limiting
- 🐳 Dockerized deployment

---

## ⚙️ Setup Instructions

### **Clone the repository & navigate to it**

```bash
git clone https://github.com/mykola-ovchynnik/goit-pythonweb-hw-12.git
cd goit-pythonweb-hw-12
```


### **Set up Environment Variables**

Create a `.env`  in the root of the project:

```ini
DATABASE_URL=postgresql+asyncpg://admin:admin@db:5432/contacts
REDIS_URL=redis://default:your_password@localhost:6379

JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256
JWT_EXPIRATION_TIME=3600
CORS_ORIGINS=http://localhost,http://127.0.0.1:8000

MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password
MAIL_FROM=your_email@example.com
MAIL_PORT=587
MAIL_SERVER=smtp.example.com
MAIL_FROM_NAME=FastAPI Contacts

CLOUDINARY_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 🐳 **Build & Run using Docker**

```ini
docker-compose up --build
```

💡 On container startup, the API will:
- Apply Alembic migrations:
```bash
alembic revision --autogenerate -m "init"

alembic upgrade head
```
- Start on http://localhost:8000

🧪 Poetry Development Mode
For local development outside Docker:
```bash
poetry install

poetry run uvicorn src.main:app --reload
```


### 🚀 **API Access**
🔑 Auth

| Method |Endpoint|Description|
|--------|---|---|
| POST   |/auth/register|Register user|
| POST   |/auth/login|Login and get JWT|
| GET    |/auth/confirm_email/{token}|Email verification|
| POST   |/auth/request_email|Re-send confirmation email|
|  POST  | /auth/request-password-reset|Request password reset|
| POST   |/auth/reset-password|Confirm password reset|

🙋‍♂️ Users

|Method|Endpoint|Description|
|---|---|---|
|GET|/users/me|Get current user info|
|PATCH|/users/avatar|Upload avatar (Cloudinary)|

📇 Contacts

|Method|Endpoint|Description|
|---|---|---|
|POST|/contacts/|Create a new contact|
|GET|/contacts/|List contacts with filtering|
|GET|/contacts/{id}|Get a specific contact|
|PATCH|/contacts/{id}|Update a contact|
|DELETE|/contacts/{id}|Delete a contact|
|GET|/contacts/search/|Search contacts by name/email|
|GET|/contacts/birthdays/|Upcoming birthdays within a given number of days|

### 🧠 Features & Middleware
- Rate Limiting: Global per-endpoint rate limit using SlowAPI
- Validation & Error Handling: Centralized exception management
- Redis Caching: Logged-in user info cached via Redis
- Gravatar Support: Auto-avatar generation fallback
- Asynchronous SQLAlchemy: Non-blocking DB operations


### 📜 **API Docs**
- Swagger UI: http://localhost:8000/docs
- ReDoc UI: http://localhost:8000/redoc

🧪 Health Check
```bash
GET /healthcheck
```

### ✨ Technologies Used
- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- Alembic
- JWT Auth
- Cloudinary (avatar uploads)
- FastMail (email verification)
- Docker + Docker Compose


