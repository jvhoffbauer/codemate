@app.get("/query")
def get_query(query):
    return f"foo bar {query}"