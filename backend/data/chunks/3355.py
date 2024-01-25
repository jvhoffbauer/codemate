@app.get("/no-alias/dict", response_model=ModelNoAlias)
def no_alias_dict():
    return {"name": "Foo"}