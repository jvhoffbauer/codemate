def test_equality() -> None:
    value1 = Default("foo")
    value2 = Default("foo")

    assert value1 == value2