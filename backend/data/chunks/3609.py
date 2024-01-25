@app.get("/items/invalidnone", response_model=Item)
def get_invalid_none():
    return None