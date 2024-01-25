@app.get(
    "/response_model_model1-annotation_model2-return_invalid_dict", response_model=User
)
def response_model_model1_annotation_model2_return_invalid_dict() -> Item:
    return {"name": "John"}