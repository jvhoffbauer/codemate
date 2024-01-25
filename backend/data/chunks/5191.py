@celery.task(name="test_celery_asyncio_cpu_bound")
def test_celery_asyncio_cpu_bound():
    # assume cpu bound
    return task_cpu_bound()