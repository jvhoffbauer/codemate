@app.get("/query/int")
def get_query_type(query: int):
    return f"foo bar {query}"