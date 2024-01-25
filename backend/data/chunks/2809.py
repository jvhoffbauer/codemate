@app.get(
    "/response_model_model1-annotation_model2-return_invalid_model", response_model=User
)
def response_model_model1_annotation_model2_return_invalid_model() -> Item:
    return Item(name="Foo", price=42.0)