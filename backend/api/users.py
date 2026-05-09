from fastapi import APIRouter, HTTPException
from typing import List
from ..models import user as user_models

router = APIRouter()

# In-memory user store for demo
_users: List[user_models.User] = []

@router.post("/", response_model=user_models.User)
def create_user(user_in: user_models.UserCreate):
    new_id = len(_users) + 1
    user = user_models.User(id=new_id, **user_in.dict(exclude={"password"}))
    _users.append(user)
    return user

# Additional endpoints (list, get) can be added similarly
