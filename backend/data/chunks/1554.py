@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}