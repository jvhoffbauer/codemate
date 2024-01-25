@app.get("/path/{param:path}")
def path_convertor(param: str = Path()):
    return {"path": param}