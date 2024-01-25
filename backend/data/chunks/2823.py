@app.get(
    "/response_model_union-no_annotation-return_model1",
    response_model=Union[User, Item],
)
def response_model_union_no_annotation_return_model1():
    return DBUser(name="John", surname="Doe", password_hash="secret")