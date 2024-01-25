@router.post("/", response_model=Job, status_code=201)
async def create_task(message: str):
    job = await redis.pool.enqueue_job("test_task", message)
    return {"id": job.job_id}