@app.get("/no_response_model-no_annotation-return_model")
def no_response_model_no_annotation_return_model():
    return User(name="John", surname="Doe")