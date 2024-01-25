def test_sync_sync_raise_other():
    with pytest.raises(OtherDependencyError):
        client.get("/sync_sync_raise_other")
    assert state["/sync_raise"] == "generator raise finalized"
    assert "/sync_raise" not in errors