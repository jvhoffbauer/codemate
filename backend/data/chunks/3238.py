@app.get("/items/objectlist", response_model=List[Item])
def get_objectlist():
    return [
        Item(name="foo", date=datetime(2021, 7, 26)),
        Item(name="bar", date=datetime(2021, 7, 26), price=1.0),
        Item(name="baz", date=datetime(2021, 7, 26), price=2.0, owner_ids=[1, 2, 3]),
    ]