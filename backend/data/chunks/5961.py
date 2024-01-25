def remove_global(*, name: str = None, alias: str = None) -> None:
    """Remove global variable"""
    if name is None and alias is None:
        __globals__.clear()
    elif name is not None and alias is None:
        for key in list(__globals__.keys()):
            if key[0] == name:
                __globals__.pop(key)
    elif name is None and alias is not None:
        for key in list(__globals__.keys()):
            if key[1] == alias:
                __globals__.pop(key)
    else:
        __globals__.pop((name, alias), None)