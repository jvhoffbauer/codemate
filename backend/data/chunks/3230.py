@app.get("/items/valid", response_model=Item)
def get_valid():
    return {"name": "valid", "date": datetime(2021, 7, 26), "price": 1.0}