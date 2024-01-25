@app.get("/items/valid", response_model=Item)
def get_valid():
    return Item(aliased_name="valid", price=1.0)