from flask import abort
from flask_apispec import doc, marshal_with, use_kwargs
from flask_jwt_extended import get_current_user, jwt_required
from webargs import fields

from app.api.api_v1.api_docs import docs, security_params
from app.core import config
from app.core.celery_app import celery_app
from app.crud.user import check_if_user_is_superuser
from app.main import app
from app.schemas.msg import MsgSchema
from app.utils import send_test_email


@docs.register
@doc(description="Test Celery worker", security=security_params, tags=["utils"])
@app.route(f"{config.API_V1_STR}/test-celery/", methods=["POST"])
@use_kwargs({"msg": fields.String(required=True)})
@marshal_with(MsgSchema())
@jwt_required
def route_test_celery(msg):
    current_user = get_current_user()  # type: User
    if not current_user:
        abort(400, "Could not authenticate user with provided token")
    elif not check_if_user_is_superuser(current_user):
        abort(400, "Not a superuser")
    celery_app.send_task("app.worker.test_celery", args=[msg])
    return ({"msg": "Word received"}, 201)


@docs.register
@doc(description="Test email", security=security_params, tags=["utils"])
@app.route(f"{config.API_V1_STR}/test-email/", methods=["POST"])
@use_kwargs({"email_to": fields.String(required=True)})
@marshal_with(MsgSchema())
@jwt_required
def route_test_email(email_to):
    current_user = get_current_user()  # type: User
    if not current_user:
        abort(400, "Could not authenticate user with provided token")
    elif not check_if_user_is_superuser(current_user):
        abort(400, "Not a superuser")
    send_test_email(email_to=email_to)
    return ({"msg": "Test email sent"}, 201)
