async def load_cache(data_id: str, data, namespace: str = None, cache_life: int = 3600):
    """Load data into the cache."""
    cache = get_cache(namespace)
    await cache.set(data_id, data, ttl=cache_life)
    LOGGER.info(f"{data_id} cache loaded")
    await cache.close()