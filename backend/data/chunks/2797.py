@app.get("/response_model_none-annotation-return_invalid_model", response_model=None)
def response_model_none_annotation_return_invalid_model() -> User:
    return Item(name="Foo", price=42.0)