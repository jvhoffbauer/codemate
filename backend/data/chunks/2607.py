@app.post("/tuple-form/")
def hello(values: Tuple[int, int] = Form()):
    return values