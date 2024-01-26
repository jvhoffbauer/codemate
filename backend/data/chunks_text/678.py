- `clean_up()` is a function that clears context variables used by Celery to prevent value reuse in subsequent tasks.
- It takes keyword arguments (`**`) and returns nothing (`-> None:`).
- The function sets two global variables, `celery_current_id` and `celery_parent_id`, both of type `Any`, to `None`. This ensures that any previously executed task's ID or parent ID are not accidentally reused for new tasks.