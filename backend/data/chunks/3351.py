@app.get("/by-alias/model", response_model=Model)
def by_alias_model():
    return Model(alias="Foo")