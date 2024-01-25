@app.get("/items/valid", response_model=Item)
def get_valid():
    return {"name": "valid", "price": 1.0}