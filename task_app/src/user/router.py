from fastapi import APIRouter, Depends
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user import controller

user_router = APIRouter(prefix='/user')

@user_router.post('/register', response_model = UserResponseSchema)
def create_new_user(body: UserSchema, db:Session = Depends(get_db)):
    return controller.createUser(body, db)


@user_router.post('/login')
def login_user(body: LoginSchema, db:Session = Depends(get_db)):
    return controller.loginUser(body, db)