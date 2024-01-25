@app.get("/path/int/{item_id}")
def get_int_id(item_id: int):
    return item_id