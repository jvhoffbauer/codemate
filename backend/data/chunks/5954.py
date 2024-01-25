def set_db(
    db: Union[Database, AsyncDatabase],
    *,
    alias: str = DEFAULT_ALIAS,
    overwrite: bool = False,
) -> bool:
    """Set database"""
    if isinstance(db, AsyncDatabase):
        return set_global(ASYNC_DB_NAME, db, alias=alias, overwrite=overwrite)
    elif isinstance(db, Database):
        return set_global(SYNC_DB_NAME, db, alias=alias, overwrite=overwrite)
    else:
        raise ValueError(f"db[{alias}] must be Database or AsyncDatabase")