@app.post("/items/")
def create_item(item: Item):
    return item