import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import crud
from app.database import Base, get_db
from app.db_models import TaskDB


# Crear una DB temporal en memoria para tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture de la DB
@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_task(db):
    task = TaskDB(title="Tarea de prueba", description="Descripción de prueba", completed=False)
    db_task = crud.create_task(db, task)
    return db_task

def test_create_task(db):
    task = TaskDB(title="Nueva tarea", description="Descripción", completed=False)
    created_task = crud.create_task(db, task)
    assert created_task.id is not None
    assert created_task.title == "Nueva tarea"

def test_get_task(db, sample_task):
    t = crud.get_task(db, sample_task.id)
    assert t.id == sample_task.id

def test_update_task(db, sample_task):
    updated_data = TaskDB(title="Actualizada", description="Nueva descripción", completed=True)
    updated = crud.update_task(db, sample_task.id, updated_data)
    assert updated.title == "Actualizada"
    assert updated.completed is True

def test_delete_task(db, sample_task):
    deleted = crud.delete_task(db, sample_task.id)
    assert deleted.id == sample_task.id
    assert crud.get_task(db, sample_task.id) is None
