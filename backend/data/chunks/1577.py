async def read_items(q: Union[list[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items