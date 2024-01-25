async def delete_by_key(key: str) -> None:
    return await redis_client.delete(key)