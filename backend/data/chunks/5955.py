def exists_db(*, alias: str = DEFAULT_ALIAS, is_async: bool = False) -> bool:
    """Judge whether the database exists"""
    if is_async:
        return exists_global(ASYNC_DB_NAME, alias=alias)
    else:
        return exists_global(SYNC_DB_NAME, alias=alias)