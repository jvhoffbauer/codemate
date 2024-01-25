@app.get(
    "/response_model_none-annotation-return_submodel_with_extra_data",
    response_model=None,
)
def response_model_none_annotation_return_submodel_with_extra_data() -> User:
    return DBUser(name="John", surname="Doe", password_hash="secret")