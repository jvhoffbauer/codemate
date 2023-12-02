from datetime import datetime

from src.enums import TodoItemVisibilityEnum
from src.models import TodoItem


def make_todo_item_create_dict(
    *,
    subject: str,
    deadline: datetime | None = None,
) -> dict[str, str | None]:
    return {
        "subject": subject,
        "deadline": _datetime_str_nullable(deadline),
    }


def make_todo_item_update_dict(
    *,
    subject: str,
    deadline: datetime | None = None,
    visibility: TodoItemVisibilityEnum = TodoItemVisibilityEnum.VISIBLE,
) -> dict[str, str | None]:
    return {
        "subject": subject,
        "deadline": _datetime_str_nullable(deadline),
        "visibility": visibility.value,
    }


def make_todo_item_response_dict(db_model: TodoItem) -> dict[str, str | int | None]:
    return {
        "id": db_model.id,
        "subject": db_model.subject,
        "deadline": _datetime_str_nullable(db_model.deadline),
        "status": db_model.status.value,
        "visibility": db_model.visibility.value,
        "resolve_time": _datetime_str_nullable(db_model.resolve_time),
    }


def _datetime_str_nullable(value: datetime | None) -> str | None:
    return value.isoformat() if value is not None else None
