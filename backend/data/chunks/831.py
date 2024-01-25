async def get_by_key(key: str) -> Optional[str]:
    return await redis_client.get(key)