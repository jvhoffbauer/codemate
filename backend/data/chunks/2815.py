@app.get(
    "/response_model_filtering_model-annotation_submodel-return_submodel",
    response_model=User,
)
def response_model_filtering_model_annotation_submodel_return_submodel() -> DBUser:
    return DBUser(name="John", surname="Doe", password_hash="secret")