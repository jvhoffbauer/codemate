def test_async_raise_raises():
    with pytest.raises(AsyncDependencyError):
        client.get("/async_raise")
    assert state["/async_raise"] == "asyncgen raise finalized"
    assert "/async_raise" in errors
    errors.clear()