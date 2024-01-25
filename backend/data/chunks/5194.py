@celery.task(name="test_celery_asyncio_io_bound")
def test_celery_asyncio_io_bound():
    async_to_sync(task_io_bound)()