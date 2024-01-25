@app.get("/no-alias/model", response_model=ModelNoAlias)
def no_alias_model():
    return ModelNoAlias(name="Foo")