async def add_cron_job(
    job_id: str = Body(..., title="任务id", embed=True),
    crontab: str = Body("*/1 * * * *", title="crontab 表达式"),
    run_time: int = Body(
        time.time(), title="第一次运行时间", description="默认立即执行", embed=True
    ),
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(
        cron_task,
        CronTrigger.from_crontab(crontab),
        args=(job_id,),
        id=job_id,  # job ID
        next_run_time=datetime.fromtimestamp(run_time),
    )
    return resp_ok(data={"job_id": schedule_job.id})