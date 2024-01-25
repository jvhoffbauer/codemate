def test_async_raise_other():
    assert state["/async_raise"] == "asyncgen raise not started"
    with pytest.raises(OtherDependencyError):
        client.get("/async_raise_other")
    assert state["/async_raise"] == "asyncgen raise finalized"
    assert "/async_raise" not in errors