@app.get(
    "/response_model_union-no_annotation-return_model2",
    response_model=Union[User, Item],
)
def response_model_union_no_annotation_return_model2():
    return Item(name="Foo", price=42.0)