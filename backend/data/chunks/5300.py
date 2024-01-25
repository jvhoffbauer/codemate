async def test_celery_async():
    celery.send_task("test_celery_asyncio_cpu_bound", args=())
    return "ok"