@app.get("/no_response_model-annotation_response_class")
def no_response_model_annotation_response_class() -> Response:
    return Response(content="Foo")