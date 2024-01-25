@app.post("/job/interval/schedule/", tags=["schedule"], summary="开启定时:间隔时间循环")
async def add_interval_job(
    seconds: int = Body(120, title="循环间隔时间/秒,默认120s", embed=True),
    job_id: str = Body(..., title="任务id", embed=True),
    run_time: int = Body(
        time.time(), title="第一次运行时间", description="默认立即执行", embed=True
    ),
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(
        cron_task,
        "interval",
        args=(job_id,),
        seconds=seconds,  # 循环间隔时间 秒
        id=job_id,  # job ID
        next_run_time=datetime.fromtimestamp(run_time),  # 立即执行
    )
    return resp_ok(data={"job_id": schedule_job.id})