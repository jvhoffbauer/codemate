@app.get(
    "/simple_exclude",
    response_model=Model2,
    response_model_exclude={"ref": {"bar"}},
)
def simple_exclude():
    return Model2(
        ref=Model1(foo="simple_exclude model foo", bar="simple_exclude model bar"),
        baz="simple_exclude model2 baz",
    )