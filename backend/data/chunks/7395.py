async def remove_schedule(job_id: str = Body(..., title="任务id", embed=True)):
    res = Schedule.get_job(job_id=job_id)
    if not res:
        return resp_fail(msg=f"not found job {job_id}")
    Schedule.remove_job(job_id)
    return resp_ok()