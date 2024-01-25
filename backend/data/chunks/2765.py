@app.get("/no_response_model-no_annotation-return_dict")
def no_response_model_no_annotation_return_dict():
    return {"name": "John", "surname": "Doe"}