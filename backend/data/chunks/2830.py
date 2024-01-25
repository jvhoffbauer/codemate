def no_response_model_annotation_union_return_model2() -> Union[User, Item]:
    return Item(name="Foo", price=42.0)