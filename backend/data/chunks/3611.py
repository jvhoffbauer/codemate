@app.get("/items/validnone", response_model=Union[Item, None])
def get_valid_none(send_none: bool = False):
    if send_none:
        return None
    else:
        return {"name": "invalid", "price": 3.2}