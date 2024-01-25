async def create_task(message: str):
    job = await redis.pool.enqueue_job("test_task", message)
    return {"id": job.job_id}