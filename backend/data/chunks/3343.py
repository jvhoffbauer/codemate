@app.get("/dict", response_model=Model, response_model_by_alias=False)
def read_dict():
    return {"alias": "Foo"}