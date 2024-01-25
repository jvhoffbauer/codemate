@app.get(
    "/simple_exclude_dict",
    response_model=Model2,
    response_model_exclude={"ref": {"bar"}},
)
def simple_exclude_dict():
    return {
        "ref": {
            "foo": "simple_exclude_dict model foo",
            "bar": "simple_exclude_dict model bar",
        },
        "baz": "simple_exclude_dict model2 baz",
    }