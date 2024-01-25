def test_not_equality() -> None:
    value1 = Default("foo")
    value2 = Default("bar")

    assert not (value1 == value2)