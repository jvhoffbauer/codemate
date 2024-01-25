@app.get("/response_model_none-annotation-return_invalid_dict", response_model=None)
def response_model_none_annotation_return_invalid_dict() -> User:
    return {"name": "John"}