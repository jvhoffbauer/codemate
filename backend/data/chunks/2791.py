@app.get("/response_model_none-annotation-return_same_model", response_model=None)
def response_model_none_annotation_return_same_model() -> User:
    return User(name="John", surname="Doe")