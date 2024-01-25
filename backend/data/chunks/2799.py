@app.get(
    "/response_model_none-annotation-return_dict_with_extra_data", response_model=None
)
def response_model_none_annotation_return_dict_with_extra_data() -> User:
    return {"name": "John", "surname": "Doe", "password_hash": "secret"}