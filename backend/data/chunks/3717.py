@app.get(
    "/simple_include_dict",
    response_model=Model2,
    response_model_include={"baz": ..., "ref": {"foo"}},
)
def simple_include_dict():
    return {
        "ref": {
            "foo": "simple_include_dict model foo",
            "bar": "simple_include_dict model bar",
        },
        "baz": "simple_include_dict model2 baz",
    }