from sqlalchemy.orm import Session
from src.user.dtos import UserSchema

def createUser(body: UserSchema, db:Session):
    print(body.model_dump())
    return {"message": "User created Successfully"}