from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..  import database, models, schemas

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = database.LocalSession()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
