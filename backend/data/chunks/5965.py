def __getattr__(name: str):
    if __faa_globals__ is not None and hasattr(__faa_globals__, name):
        return getattr(__faa_globals__, name)
    elif name == SYNC_DB_NAME:
        return get_sync_db()
    elif name == ASYNC_DB_NAME:
        return get_async_db()
    elif name == SITE_NAME:
        return get_site()
    elif exists_global(name, alias=DEFAULT_ALIAS):
        return get_global(name, alias=DEFAULT_ALIAS)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")