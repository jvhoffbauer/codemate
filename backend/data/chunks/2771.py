@app.get("/response_model-no_annotation-return_invalid_dict", response_model=User)
def response_model_no_annotation_return_invalid_dict():
    return {"name": "John"}