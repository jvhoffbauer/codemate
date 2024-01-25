@app.get("/jobs/all", tags=["schedule"], summary="获取所有job信息")
async def get_scheduled_syncs():
    """
    获取所有job
    :return:
    """
    schedules = []
    for job in Schedule.get_jobs():
        schedules.append(
            {
                "job_id": job.id,
                "func_name": job.func_ref,
                "func_args": job.args,
                "cron_model": str(job.trigger),
                "next_run": str(job.next_run_time),
            }
        )
    return resp_ok(data=schedules)