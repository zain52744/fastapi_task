from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import UserCreate
# from app.core.dependencies import get_user_count

router = APIRouter(prefix="/users", tags=["Users"])

users_db = []

@router.post("/add_user")
async def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {
        "id": user_id,
        "name": user.name,  
        "age": user.age     
    }
    users_db.append(new_user)
    return new_user

@router.get("/get_user")
async def get_users():
    if not users_db:
        raise HTTPException(status_code=404, detail="No users found")
    return users_db

