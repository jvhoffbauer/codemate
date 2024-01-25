@app.get("/int/{param:int}")
def int_convertor(param: int = Path()):
    return {"int": param}