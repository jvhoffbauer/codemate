@app.get("/path/bool/{item_id}")
def get_bool_id(item_id: bool):
    return item_id