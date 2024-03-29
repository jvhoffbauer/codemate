- Endpoint for scheduling a one-time task with fixed execution time using FastAPI and Celery Beat
- Accepts two parameters `run_time` (UNIX timestamp of when to execute the task) and `job_id` (unique identifier for the scheduled task) in request body
- Checks whether the specified `job_id` is already registered; returns error message if found
- Creates a new Celery Beat job with `cron_task` as its callback function, executes once at the given `run_time`, and sets `job_id` as its unique identifier
- Returns success response containing the newly created job's ID