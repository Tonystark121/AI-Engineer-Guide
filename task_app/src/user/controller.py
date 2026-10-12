from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException

from src.user.dtos import UserSchema
from src.user.models import UserModal
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


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