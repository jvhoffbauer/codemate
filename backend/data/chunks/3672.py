@app.get("/foo")
def foo():
    return {"message": "Hello World"}