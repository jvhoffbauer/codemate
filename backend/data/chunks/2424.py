def read_items(q: List[int] = Query(default=None)):
    return {"q": q}