async def hidden_query(
    hidden_query: Optional[str] = Query(default=None, include_in_schema=False)
):
    return {"hidden_query": hidden_query}