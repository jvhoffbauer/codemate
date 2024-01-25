@app.post("/foo")
def foo(items: Items):
    return items.items