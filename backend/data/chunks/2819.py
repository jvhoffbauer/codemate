@app.get("/no_response_model-annotation_list_of_model")
def no_response_model_annotation_list_of_model() -> List[User]:
    return [
        DBUser(name="John", surname="Doe", password_hash="secret"),
        DBUser(name="Jane", surname="Does", password_hash="secret2"),
    ]