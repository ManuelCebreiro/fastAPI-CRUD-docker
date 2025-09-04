from sqlalchemy.orm import Session

from app.db_models import TaskDB


def get_all_tasks(db : Session):
    return db.query(TaskDB).all()

def get_task(db: Session, task_id: int):
    return db.query(TaskDB).filter(TaskDB.id == task_id).first()

def create_task(db: Session, task: TaskDB):
    db_task = TaskDB(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, updated_task: TaskDB):
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if db_task:
        db_task.title = updated_task.title
        db_task.description = updated_task.description
        db_task.completed = updated_task.completed
        db.commit()
        db.refresh(db_task)
        return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not db_task:
        return None
    
    db.delete(db_task)
    db.commit()
    return db_task