from fastapi import APIRouter, Depends
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user import controller

user_router = APIRouter(prefix='/user')

@user_router.post('/create')
def create_new_user(body: UserSchema, db:Session = Depends(get_db)):
    print('router called', body.model_dump())
    return controller.createUser(body, db)