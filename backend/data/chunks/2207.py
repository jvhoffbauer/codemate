@app.get("/path/str/{item_id}")
def get_str_id(item_id: str):
    return item_id