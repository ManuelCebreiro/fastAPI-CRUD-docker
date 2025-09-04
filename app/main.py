from fastapi import FastAPI

from app.database import Base, engine
from app.db_models import TaskDB
from app.routers import tasks

app = FastAPI()

app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])

#Crear tablas al inicio si no existen

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"Message": "¡FastAPI + Docker + CRUD en memoria funcionando"}
