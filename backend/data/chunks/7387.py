async def get_target_sync(job_id: str = Query("job1", title="任务id")):
    job = Schedule.get_job(job_id=job_id)

    if not job:
        return resp_fail(msg=f"not found job {job_id}")

    return resp_ok(
        data={
            "job_id": job.id,
            "func_name": job.func_ref,
            "func_args": job.args,
            "cron_model": str(job.trigger),
            "next_run": str(job.next_run_time),
        }
    )