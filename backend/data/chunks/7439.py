async def remove_schedule(job_id: str = Body(..., title="job_id", embed=True)):
    res = schedule.get_job(job_id=job_id)
    if not res:
        return resp.fail(resp.DataNotFound.set_msg(f"not found job {job_id}"))

    schedule.remove_job(job_id)

    return resp.ok()