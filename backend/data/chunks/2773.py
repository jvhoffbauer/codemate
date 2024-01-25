@app.get("/response_model-no_annotation-return_invalid_model", response_model=User)
def response_model_no_annotation_return_invalid_model():
    return Item(name="Foo", price=42.0)