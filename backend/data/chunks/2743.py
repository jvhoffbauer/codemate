@app.get("/explicit-query")
def read_explicit_query(q: Union[str, None] = Query()):
    return q