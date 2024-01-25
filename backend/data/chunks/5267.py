    @classmethod
    async def create(cls):
        _pool = await aioredis.Redis(host=settings.REDIS_CACHE_URI)
        return cls(pool=_pool)