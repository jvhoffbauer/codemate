def mixed():
    return Model3(
        name="mixed model3 name",
        age=3,
        ref2=Model2(
            ref=Model1(foo="mixed model foo", bar="mixed model bar"),
            baz="mixed model2 baz",
        ),
    )