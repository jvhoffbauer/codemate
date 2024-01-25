def get_async_db(*, alias: str = DEFAULT_ALIAS) -> AsyncDatabase:
    """Get async database"""
    if exists_global(ASYNC_DB_NAME, alias=alias):
        return get_global(ASYNC_DB_NAME, alias=alias)
    if exists_site(alias=alias):
        db = get_site(alias=alias).db
        if isinstance(db, AsyncDatabase):
            return db
    raise ValueError(f"async_db[{alias}] not found, please call `set_db` first")