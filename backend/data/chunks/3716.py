def simple_include():
    return Model2(
        ref=Model1(foo="simple_include model foo", bar="simple_include model bar"),
        baz="simple_include model2 baz",
    )