@app.post("/job/date/schedule/", tags=["schedule"], summary="开启定时:固定只运行一次时间")
async def add_date_job(
    run_time: int = Body(..., title="时间戳", description="固定只运行一次时间", embed=True),
    job_id: str = Body(..., title="任务id", embed=True),
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(
        cron_task,
        "date",
        args=(job_id,),
        run_date=datetime.fromtimestamp(run_time),
        id=job_id,  # job ID
    )
    return resp_ok(data={"job_id": schedule_job.id})