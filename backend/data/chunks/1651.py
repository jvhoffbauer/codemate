async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items