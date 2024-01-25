def test_celery(
    msg: schemas.Msg,
) -> Any:
    """Test Celery worker."""
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}