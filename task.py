from fastapi import APIRouter
from ..schemas import CreateTask, UpdateTask

router = APIRouter(
    prefix="/task",
    tags=["task"],
)


@router.get("/")
def all_tasks():
    pass


@router.get("/{task_id}")
def task_by_id(task_id: int):
    pass


@router.post("/create")
def create_task(task: CreateTask):
    pass


@router.put("/update/{task_id}")
def update_task(task_id: int, task: UpdateTask):
    pass


@router.delete("/delete/{task_id}")
def delete_task(task_id: int):
    pass
