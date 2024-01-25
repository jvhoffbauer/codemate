@app.get("/response_model_none-annotation-return_exact_dict", response_model=None)
def response_model_none_annotation_return_exact_dict() -> User:
    return {"name": "John", "surname": "Doe"}