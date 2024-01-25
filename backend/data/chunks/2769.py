@app.get("/response_model-no_annotation-return_exact_dict", response_model=User)
def response_model_no_annotation_return_exact_dict():
    return {"name": "John", "surname": "Doe"}