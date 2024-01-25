@app.get("/path/float/{item_id}")
def get_float_id(item_id: float):
    return item_id