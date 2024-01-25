async def get_task(task_id: str):
    job = ArqJob(task_id, redis.pool)
    return await job.info()