from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
