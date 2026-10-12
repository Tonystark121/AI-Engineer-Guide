from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException

from src.user.dtos import UserSchema, LoginSchema
from src.user.models import UserModal
from pwdlib import PasswordHash
from src.utils.settings import setting
import jwt


password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def createUser(body: UserSchema, db: Session):
    # Check if username, email, or phone already exists
    check_user = db.query(UserModal).filter(
        or_(
            UserModal.username == body.username,
            UserModal.email == str(body.email),
            UserModal.phone == body.phone
        )
    ).first()

    if check_user:
        if check_user.username == body.username:
            raise HTTPException(
                status_code=409,
                detail="Username already exists"
            )

        if check_user.email == str(body.email):
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        if check_user.phone == body.phone:
            raise HTTPException(
                status_code=409,
                detail="Phone number already exists"
            )

    # Hash the password before saving
    hashed_password = get_password_hash(body.password)

    new_user = UserModal(
        name=body.name,
        phone=body.phone,
        email=str(body.email),
        username=body.username,
        hashpasswd=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except Exception:
        db.rollback()
        raise
    
def loginUser(body: LoginSchema, db:Session):
    check_user = db.query(UserModal).filter(UserModal.username == body.username).first()
    if not check_user: 
        return HTTPException(404, 'No such user exist, please enter correct details')
    
    if not verify_password(body.password, check_user.hashpasswd):
        return HTTPException(404, 'incorrect passwd, please enter correct details')
    
    token = jwt.encode({"id":check_user.id, "username": check_user.username }, setting.SECRET_KEY, setting.ALGORITHM)
    
    
    return token