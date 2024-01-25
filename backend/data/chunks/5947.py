def get_sync_db(*, alias: str = DEFAULT_ALIAS) -> Database:
    """Get sync database"""
    if exists_global(SYNC_DB_NAME, alias=alias):
        return get_global(SYNC_DB_NAME, alias=alias)
    if exists_site(alias=alias):
        db = get_site(alias=alias).db
        if isinstance(db, Database):
            return db
    raise ValueError(f"sync_db[{alias}] not found, please call `set_db` first")