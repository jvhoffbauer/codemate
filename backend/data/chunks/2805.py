@app.get(
    "/response_model_model1-annotation_model2-return_exact_dict", response_model=User
)
def response_model_model1_annotation_model2_return_exact_dict() -> Item:
    return {"name": "John", "surname": "Doe"}