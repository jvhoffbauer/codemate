@app.get("/by-alias/list", response_model=List[Model])
def by_alias_list():
    return [{"alias": "Foo"}, {"alias": "Bar"}]