@app.get(
    "/response_model-no_annotation-return_submodel_with_extra_data", response_model=User
)
def response_model_no_annotation_return_submodel_with_extra_data():
    return DBUser(name="John", surname="Doe", password_hash="secret")