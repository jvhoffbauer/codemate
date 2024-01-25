@app.get("/no_response_model-annotation_json_response_class")
def no_response_model_annotation_json_response_class() -> JSONResponse:
    return JSONResponse(content={"foo": "bar"})