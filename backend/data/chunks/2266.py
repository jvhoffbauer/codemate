def get_query_param_required_type(query: int = Query()):
    return f"foo bar {query}"