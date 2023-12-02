from pydantic import ConstrainedStr, EmailStr, Field, SecretStr

from .base import BaseAPIModel


class UsernameType(ConstrainedStr):
    min_length = 2
    regex = "^[a-z0-9_.-]+$"


class UserUpdate(BaseAPIModel):
    username: UsernameType = Field(example="john.doe")
    full_name: str | None = Field(example="John Doe", default=None)


class UserCreate(BaseAPIModel):
    username: UsernameType = Field(example="john.doe")
    email: EmailStr = Field(example="john.doe@mail.com")
    full_name: str | None = Field(example="John Doe", default=None)
    password: SecretStr = Field(min_length=8, example="XZ#o2Q#eQ3y1")


class UserResponse(BaseAPIModel):
    id: int = Field(example=1)
    username: str = Field(example="john.doe")
    email: str = Field(example="john.doe@mail.com")
    full_name: str | None = Field(example="John Doe")

    class Config:
        orm_mode = True
