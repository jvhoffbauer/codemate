@app.get("/no_response_model-annotation-return_invalid_dict")
def no_response_model_annotation_return_invalid_dict() -> User:
    return {"name": "John"}