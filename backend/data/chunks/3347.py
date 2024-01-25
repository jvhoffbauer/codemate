@app.get("/list", response_model=List[Model], response_model_by_alias=False)
def read_list():
    return [{"alias": "Foo"}, {"alias": "Bar"}]