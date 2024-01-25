@app.get("/no_response_model-annotation-return_dict_with_extra_data")
def no_response_model_annotation_return_dict_with_extra_data() -> User:
    return {"name": "John", "surname": "Doe", "password_hash": "secret"}