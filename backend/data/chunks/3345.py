@app.get("/model", response_model=Model, response_model_by_alias=False)
def read_model():
    return Model(alias="Foo")