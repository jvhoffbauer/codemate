def no_response_model_annotation_return_invalid_model() -> User:
    return Item(name="Foo", price=42.0)