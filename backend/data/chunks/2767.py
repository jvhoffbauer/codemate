@app.get("/response_model-no_annotation-return_same_model", response_model=User)
def response_model_no_annotation_return_same_model():
    return User(name="John", surname="Doe")