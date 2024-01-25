async def add_job_to_scheduler(
    *,
    seconds: int = Body(120, title="循环间隔时间/秒,默认120s", embed=True),
    job_id: str = Body(..., title="任务id", embed=True),
):
    """
    简易的任务调度演示 可自行参考文档 https://apscheduler.readthedocs.io/en/stable/
    三种模式
    date: use when you want to run the job just once at a certain point of time
    interval: use when you want to run the job at fixed intervals of time
    cron: use when you want to run the job periodically at certain time(s) of day
    :param seconds:
    :param job_id:
    :return:
    """
    res = schedule.get_job(job_id=job_id)
    if res:
        return resp.fail(resp.InvalidRequest.set_msg(f"{job_id} job already exists"))

    schedule_job = schedule.add_job(
        demo_task,
        "interval",
        args=(job_id,),
        seconds=seconds,  # 循环间隔时间 秒
        id=job_id,  # job ID
        next_run_time=datetime.now(),  # 立即执行
    )
    return resp.ok(data={"id": schedule_job.id})