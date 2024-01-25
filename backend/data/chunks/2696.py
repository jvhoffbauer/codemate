@app.post("/items/")
def save_item_no_body(item: List[Item]):
    return {"item": item}