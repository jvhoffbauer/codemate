async def close_redis_pool():
    redis.pool.close()