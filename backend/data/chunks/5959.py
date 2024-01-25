def exists_global(name: str, *, alias: str = DEFAULT_ALIAS) -> bool:
    """Judge whether the global variable exists"""
    return (name, alias) in __globals__ or (
        alias == DEFAULT_ALIAS and _exists_faa_global(name)
    )