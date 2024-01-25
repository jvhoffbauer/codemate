@app.post("/items/")
def save_union_body(item: Union[OtherItem, Item]):
    return {"item": item}