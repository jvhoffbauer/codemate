def test_sync_async_raise_other():
    with pytest.raises(OtherDependencyError):
        client.get("/sync_async_raise_other")
    assert state["/async_raise"] == "asyncgen raise finalized"
    assert "/async_raise" not in errors