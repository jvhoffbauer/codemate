from datetime import datetime
from typing import Any

from pydantic import Field, validator

from src.enums import TodoItemStatusEnum, TodoItemVisibilityEnum

from .base import BaseAPIModel


class TodoItemCreate(BaseAPIModel):
    subject: str = Field(example="finish FastAPI tutorial")
    deadline: datetime | None = Field(
        example=datetime(2023, 6, 1, 18, 0, 0), default=None
    )

    @validator("deadline")
    def validate_deadline(
        cls, v: datetime | None, values: dict[str, Any], **kwargs: Any
    ) -> datetime | None:
        if v is not None and v < datetime.now():
            raise ValueError("must be only in the future")
        return v


class TodoItemUpdate(BaseAPIModel):
    subject: str = Field(example="finish FastAPI tutorial")
    deadline: datetime | None = Field(example=datetime(2023, 6, 1, 18, 0, 0))
    visibility: TodoItemVisibilityEnum = Field(example=TodoItemVisibilityEnum.ARCHIVED)


class TodoItemResponse(BaseAPIModel):
    id: int = Field(example=1)
    subject: str = Field(example="finish FastAPI tutorial")
    deadline: datetime | None = Field(example=datetime(2023, 6, 1, 18, 0, 0))
    status: TodoItemStatusEnum = Field(example=TodoItemStatusEnum.OPEN)
    visibility: TodoItemVisibilityEnum = Field(example=TodoItemVisibilityEnum.VISIBLE)
    resolve_time: datetime | None = Field(example=datetime(2023, 5, 10, 14, 23, 18))

    class Config:
        orm_mode = True
