def mixed_dict():
    return {
        "name": "mixed_dict model3 name",
        "age": 3,
        "ref2": {
            "ref": {"foo": "mixed_dict model foo", "bar": "mixed_dict model bar"},
            "baz": "mixed_dict model2 baz",
        },
    }