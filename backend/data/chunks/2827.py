@app.get("/no_response_model-annotation_union-return_model1")
def no_response_model_annotation_union_return_model1() -> Union[User, Item]:
    return DBUser(name="John", surname="Doe", password_hash="secret")