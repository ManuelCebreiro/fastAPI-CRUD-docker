# FastAPI CRUD + PostgreSQL + Docker

Proyecto de ejemplo de API REST para gestión de tareas (ToDo) usando **FastAPI**, **PostgreSQL** y **Docker**.  
Diseñado como proyecto demostrativo de **Full Stack + Docker + Persistencia de datos + CI/CD**.

---

## 🛠 Tecnologías

- **Backend:** FastAPI, Python 3.11  
- **Base de datos:** PostgreSQL 15  
- **Docker:** Contenedores y volúmenes para desarrollo y persistencia  
- **ORM:** SQLAlchemy  
- **Dependencias:** Poetry o pip  
- **Testing:** pytest (para demostrar CI/CD con GitHub Actions)  

---

## 🚀 Funcionalidades

- Crear, listar, actualizar y eliminar tareas (CRUD)  
- Persistencia de datos en PostgreSQL  
- Volúmenes Docker para mantener la base de datos entre reinicios  
- Documentación automática con Swagger: `/docs`  
- Health check: `/health`  

---

## 📦 Requisitos

- Docker & Docker Compose  
- Python 3.11 (si quieres correr fuera de Docker)  

---

## ⚡ Cómo usarlo

1. **Clonar el repositorio**:

```bash
git clone <URL_DEL_REPO>
cd fastapi-crud-docker

Crear archivo .env con tus credenciales:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks_db
POSTGRES_HOST=db
POSTGRES_PORT=5432


Levantar la app con Docker Compose:

docker-compose up --build


Acceder a la API:

Swagger UI: http://localhost:8000/docs

Health check: http://localhost:8000/health

🧪 Tests (opcional)

Si agregas tests con pytest:

docker exec -it fastapi-crud-docker-web-1 pytest

⚙️ CI/CD

Este proyecto tiene integrado un flujo básico de GitHub Actions para:

Levantar un servicio PostgreSQL temporal

Instalar dependencias con Poetry

Ejecutar migraciones con Alembic

Correr tests automáticamente

Archivo de workflow: .github/workflows/python-app.yml

📁 Estructura del proyecto
fastapi-crud-docker/
│
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ routers/
│  ├─ db_models.py
│  ├─ crud.py
│  ├─ database.py
│
├─ create_tables.py         # Script opcional para crear tablas manualmente
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .env
├─ pyproject.toml
└─ .gitignore

testing