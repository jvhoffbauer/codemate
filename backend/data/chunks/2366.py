@app.get("/items/coerce", response_model=Item)
def get_coerce():
    return Item(aliased_name="coerce", price="1.0")