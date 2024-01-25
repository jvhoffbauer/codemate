@shared_task()
def task2():
    logger.info("test2")
    task3.delay()