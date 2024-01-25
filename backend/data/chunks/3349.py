@app.get("/by-alias/dict", response_model=Model)
def by_alias_dict():
    return {"alias": "Foo"}