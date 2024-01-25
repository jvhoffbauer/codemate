def test_default():
    """test default dep behavior."""

    @dataclass
    class dep(dependencies.DefaultDependency):
        v: int

    # make sure we can unpack the class
    assert dict(**dep(v=1)) == {"v": 1}
    assert dep(v=1).v == 1