def test_celery():
    celery.send_task("test_celery", args=("words????",))
    return "ok"