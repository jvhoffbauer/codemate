@shared_task
def task1():
    logger.info("test1")
    task2.delay()