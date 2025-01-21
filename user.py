from fastapi import APIRouter
from ..schemas import CreateUser, UpdateUser

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
def all_users():
    pass


@router.get("/{user_id}")
def user_by_id(user_id: int):
    pass


@router.post("/create")
def create_user(user: CreateUser):
    pass


@router.put("/update/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    pass


@router.delete("/delete/{user_id}")
def delete_user(user_id: int):
    pass

