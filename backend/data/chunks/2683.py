@app.put("/items/{item_id}")
def save_item_no_body(item_id: str):
    return {"item_id": item_id}