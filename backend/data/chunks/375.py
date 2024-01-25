def test_not_equality_other() -> None:
    value1 = Default("foo")
    value2 = "foo"

    assert not (value1 == value2)