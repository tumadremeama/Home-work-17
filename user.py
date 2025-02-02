from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db import get_db
from app.models.user2 import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import Annotated

router = APIRouter(prefix='/user', tags=['user'])


@router.get("/", response_model=list[CreateUser])
def all_users(db: Annotated[Session, Depends(get_db)]):
    query = select(User)
    users = db.scalars(query).all()
    return users


@router.get("/{user_id}", response_model=CreateUser)
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    query = select(User).where(User.id == user_id)
    user = db.scalars(query).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(user_data.username)

    existing_user = db.scalars(select(User).where(User.username == user_data.username)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    new_user = User(
        username=user_data.username,
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        age=user_data.age,
        slug=slug
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}")
def update_user(user_id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    user = db.scalars(query).first()

    if user:
        update_query = (
            update(User).
            where(User.id == user_id).
            values(
                firstname=user_data.firstname,
                lastname=user_data.lastname,
                age=user_data.age
            )
        )
        db.execute(update_query)
        db.commit()

        return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")


@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):

    query = select(User).where(User.id == user_id)
    user = db.scalars(query).first()

    if user:
        delete_query = delete(User).where(User.id == user_id)
        db.execute(delete_query)
        db.commit()

        return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

