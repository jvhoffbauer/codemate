@app.get("/", response_model=Model3)
def f():
    return {"c": {}, "d": {"a": {}}}