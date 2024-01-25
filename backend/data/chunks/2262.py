def get_query_param(query=Query(default=None)):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"