- Defines a new endpoint `/test-celery` using FastAPI's router decorator
- Uses dependency injection to ensure that only authenticated superusers can access this endpoint
- Accepts an instance of the `Msg` schema as input and returns a simple message confirming receipt of the data
- Sends a task to the Celery queue using the `send_task()` method provided by Celery's app object (in this case, `celery_app`) with arguments containing the received message