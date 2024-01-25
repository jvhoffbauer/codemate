@app.get("/float/{param:float}")
def float_convertor(param: float = Path()):
    return {"float": param}