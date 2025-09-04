from app.database import Base, engine
from app.db_models import TaskDB

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")
