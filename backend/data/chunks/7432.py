@router.get("/jobs/all", summary="获取所有job信息", name="获取所有定时任务")
async def get_scheduled_syncs():
    """
    获取所有job
    :return:
    """
    schedules = []
    for job in schedule.get_jobs():
        schedules.append(
            {
                "job_id": job.id,
                "func_name": job.func_ref,
                "func_args": job.args,
                "cron_model": str(job.trigger),
                "next_run": str(job.next_run_time),
            }
        )

    return resp.ok(data=schedules)