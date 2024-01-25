@app.get(
    "/response_model_model1-annotation_model2-return_submodel_with_extra_data",
    response_model=User,
)
def response_model_model1_annotation_model2_return_submodel_with_extra_data() -> Item:
    return DBUser(name="John", surname="Doe", password_hash="secret")