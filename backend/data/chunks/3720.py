def simple_exclude():
    return Model2(
        ref=Model1(foo="simple_exclude model foo", bar="simple_exclude model bar"),
        baz="simple_exclude model2 baz",
    )