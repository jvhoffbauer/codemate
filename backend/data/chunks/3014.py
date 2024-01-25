def get_something_else(*, someheader: str = Depends(get_header)):
    return f"{someheader}123"