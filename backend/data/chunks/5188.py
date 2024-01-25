@celery.task(name="test_celery")
def test_celery(word: str) -> str:
    f = f"test_celery {word}"
    print(f)
    return f