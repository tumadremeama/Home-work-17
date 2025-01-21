from fastapi import FastAPI
from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}