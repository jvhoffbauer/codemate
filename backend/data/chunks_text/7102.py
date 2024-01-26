- This endpoint allows scheduling a new cron job with a given `job_id`, `crontab` expression, and optional initial execution time (default is immediate).
- The function first checks whether the specified `job_id` already has an existing scheduled task using `Schedule.get_job()`. If so, it returns an error message; otherwise, it proceeds to create a new scheduled job using `Schedule.add_job()`.
- The created job's details are returned in the response body as JSON data under the key "job_id".