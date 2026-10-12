import re
from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator

class UserSchema(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    phone: str = Field(pattern=r"^[0-9]{10}$")
    email: EmailStr
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9]+$"
    )
    password: str = Field(min_length=4, max_length=128)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()