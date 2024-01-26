- Defines a function `add_cron_job()` that adds a new scheduled task to the system using Celery Beat's scheduler (Schedule).
- Takes three arguments: `job_id`, `crontab`, and `run_time`. These are passed as keyword arguments with descriptive titles for clarity in documentation and error messages.
- Checks whether a job with the given `job_id` already exists by calling `Schedule.get_job()`. If it does, returns an error message; otherwise proceeds with adding the new job.
- Creates a new scheduled task using `Schedule.add_job()` with the specified `CronTrigger` generated from the `crontab` argument. The `args` parameter is set to a tuple containing the `job_id` value.
- Sets the unique identifier of the newly created job as its `id` property. This can be used later to retrieve or delete specific jobs.
- Specifies the initial execution time of the job using the `next_run_time` parameter, which takes a datetime object representing the Unix timestamp of the desired start time. In this case, we use the current time unless another value is provided via the `Body()` decorator.