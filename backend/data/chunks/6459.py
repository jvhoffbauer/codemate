def get_cache(namespace) -> Union[aiocache.RedisCache, aiocache.SimpleMemoryCache]:
    """Retunr"""
    if REDIS_URL:
        LOGGER.info("using RedisCache")
        return aiocache.RedisCache(
            endpoint=REDIS_URL.host,
            port=REDIS_URL.port,
            password=REDIS_URL.password,
            namespace=namespace,
            create_connection_timeout=5,
        )
    LOGGER.info("using SimpleMemoryCache")
    return aiocache.SimpleMemoryCache(namespace=namespace)