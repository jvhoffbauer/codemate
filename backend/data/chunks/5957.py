def get_global(name: str, *, alias: str = DEFAULT_ALIAS) -> Any:
    """Get global variable"""
    if (name, alias) not in __globals__:
        if alias == DEFAULT_ALIAS and _exists_faa_global(name):
            return getattr(__faa_globals__, name)
        raise ValueError(
            f"global[{name},{alias}] not found, please call `set_global` first"
        )
    return __globals__[(name, alias)]