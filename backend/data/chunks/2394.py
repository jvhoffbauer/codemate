@app.get("/query/")
def query_convertor(param: str = Query()):
    return {"query": param}