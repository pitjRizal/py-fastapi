project/
│
├── app/
│   ├── main.py
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   ├── security.py
│   │   └── rate_limiter.py
│   │
│   ├── middleware/
│   │   ├── cors.py
│   │   ├── auth.py
│   │   └── timeout.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── migrations/      <-- Alembic untuk menangani migrasi db
│   │
│   ├── models/              <-- SQLAlchemy/SQLModel models
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── schemas/             <-- Pydantic schemas
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── repositories/        <-- Database queries (repository pattern)
│   │   ├── user_repo.py
│   │   └── __init__.py
│   │
│   ├── services/            <-- Business logic
│   │   ├── user_service.py
│   │   └── __init__.py
│   │
│   ├── routes/              <-- API routers 
│   │   ├── __init__.py
│   │   ├── index.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   └── auth.py
│   │   └── v2/
│   │       └── users.py
│   │
│   ├── tasks/               <-- Background tasks / Celery / RQ
│   │   └── send_email.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   ├── response.py
│   │   └── pagination.py
│   │
│   ├── static/
│   └── templates/
│
├── tests/
│   ├── test_users.py
│   └── conftest.py
│
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml (optional)
