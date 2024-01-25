@app.get("/items/no-response-model/object")
def get_no_response_model_object():
    return Item(
        name="object", date=datetime(2021, 7, 26), price=1.0, owner_ids=[1, 2, 3]
    )