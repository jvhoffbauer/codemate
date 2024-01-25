@celery_app.task(acks_late=True)
def test_celery(word: str):
    return f"test task return {word}"