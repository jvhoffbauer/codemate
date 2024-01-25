@app.get("/query")
def read_query(q: Union[str, None]):
    return q