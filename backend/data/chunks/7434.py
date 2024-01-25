@router.get("/jobs/once", summary="获取指定的job信息", name="获取指定定时任务")
async def get_target_sync(job_id: str = Query(..., title="任务id")):
    job = schedule.get_job(job_id=job_id)

    if not job:
        return resp.fail(resp.DataNotFound.set_msg(f"not found job {job_id}"))

    return resp.ok(
        data={
            "job_id": job.id,
            "func_name": job.func_ref,
            "func_args": job.args,
            "cron_model": str(job.trigger),
            "next_run": str(job.next_run_time),
        }
    )