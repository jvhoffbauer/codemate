@app.get(
    "/mixed",
    response_model=Model3,
    response_model_include={"ref2", "name"},
    response_model_exclude={"ref2": {"baz"}},
)
def mixed():
    return Model3(
        name="mixed model3 name",
        age=3,
        ref2=Model2(
            ref=Model1(foo="mixed model foo", bar="mixed model bar"),
            baz="mixed model2 baz",
        ),
    )