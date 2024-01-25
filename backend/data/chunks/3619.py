@app.get("/valid2", responses={"500": {"model": List[int]}})
def valid2():
    pass