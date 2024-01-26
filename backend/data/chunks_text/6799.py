- This endpoint receives a message from the client and sends it to a Celery task using `celery_app.send_task()`.
- The `args` parameter of `send_task()` is used to pass the message as an argument to the Celery task function `test_celery()` in the app module.
- The method returns a success message to the client immediately after sending the task to Celery.