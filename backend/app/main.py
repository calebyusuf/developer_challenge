from fastapi import FastAPI
from .routers import tasks
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
              title=" HMCTS Task API",
              descriiption="API for creating tasks",
              version="1.0.0"
          )

app.include_router(tasks.router)

