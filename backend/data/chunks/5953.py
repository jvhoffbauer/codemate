def get_db(
    *, alias: str = DEFAULT_ALIAS, is_async: bool = False
) -> Union[Database, AsyncDatabase]:
    """Get database"""
    if is_async:
        return get_async_db(alias=alias)
    return get_sync_db(alias=alias)