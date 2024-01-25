@app.get("/valid1", responses={"500": {"model": int}})
def valid1():
    pass