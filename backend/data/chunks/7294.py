@router.post(
    "/test-celery",
    response_model=schemas.Msg,
    status_code=201,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def test_celery(
    msg: schemas.Msg,
) -> Any:
    """Test Celery worker."""
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}