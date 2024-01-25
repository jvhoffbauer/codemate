@app.get("/query/param-required")
def get_query_param_required(query=Query()):
    return f"foo bar {query}"