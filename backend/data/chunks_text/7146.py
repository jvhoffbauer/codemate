- This endpoint starts a scheduled job using APScheduler library in FastAPI framework.
- It accepts two parameters `seconds` and `job_id`. The former specifies the looping interval time (in seconds) for the task, while the latter is the unique identifier assigned to the job.
- If the specified job ID already exists, an error message is returned. Otherwise, a new job with the given arguments is added to the scheduler.
- The function returns a JSON response containing the ID of the newly created job.