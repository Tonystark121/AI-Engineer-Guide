from sqlalchemy.orm import Session
from fastapi import HTTPException, Request, Depends
from src.utils.settings import setting
import jwt
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModal
from src.utils.db import get_db

def isAuthroized(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get('authorization')
    if not token:
        raise HTTPException(
                    status_code=401,
                    detail="Invalid or expired token"
                )
        
    token = token.split(" ")[-1]
    
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    user_id = payload.get("sub", payload.get("id"))
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )
    user = db.query(UserModal).filter(UserModal.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found. Access denied."
        )
        
    return user