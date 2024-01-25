async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items