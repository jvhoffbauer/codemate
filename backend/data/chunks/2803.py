@app.get(
    "/response_model_model1-annotation_model2-return_same_model", response_model=User
)
def response_model_model1_annotation_model2_return_same_model() -> Item:
    return User(name="John", surname="Doe")