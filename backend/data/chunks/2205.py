@app.get("/path/{item_id}")
def get_id(item_id):
    return item_id