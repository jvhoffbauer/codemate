@app.get("/no-alias/list", response_model=List[ModelNoAlias])
def no_alias_list():
    return [{"name": "Foo"}, {"name": "Bar"}]