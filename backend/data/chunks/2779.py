@app.get("/no_response_model-annotation-return_same_model")
def no_response_model_annotation_return_same_model() -> User:
    return User(name="John", surname="Doe")