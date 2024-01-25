@app.get("/no_response_model-annotation-return_exact_dict")
def no_response_model_annotation_return_exact_dict() -> User:
    return {"name": "John", "surname": "Doe"}