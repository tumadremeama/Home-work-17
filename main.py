from fastapi import FastAPI
from app.backend.db import Base, engine
from app.routers import user, task

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключение роутеров
app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}