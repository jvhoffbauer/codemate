def read_items(q: Optional[str] = Param(default=None)):  # type: ignore
    return {"q": q}