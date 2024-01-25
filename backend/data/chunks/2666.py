@app.get("/foo", response_model=Item)
def foo():
    return {"name": "Foo item"}