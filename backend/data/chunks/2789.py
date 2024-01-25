@app.get("/no_response_model-annotation-return_submodel_with_extra_data")
def no_response_model_annotation_return_submodel_with_extra_data() -> User:
    return DBUser(name="John", surname="Doe", password_hash="secret")