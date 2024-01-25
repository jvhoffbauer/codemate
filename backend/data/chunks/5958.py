def set_global(
    name: str,
    value: Any,
    *,
    alias: str = DEFAULT_ALIAS,
    overwrite: bool = False,
) -> bool:
    """Set global variable"""
    if exists_global(name, alias=alias) and not overwrite:
        return False
    __globals__[(name, alias)] = value
    return True