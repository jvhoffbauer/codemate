@bp.get("/test_celery_asyncio_io_bound")
async def test_celery_async():
    celery.send_task("test_celery_asyncio_io_bound", args=())
    return "ok"