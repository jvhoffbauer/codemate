async def check_cache(data_id: str, namespace: str = None):
    """Check the data of a cache given an id."""
    cache = get_cache(namespace)
    result = await cache.get(data_id, None)
    LOGGER.info(f"{data_id} cache pulled")
    await cache.close()
    return result