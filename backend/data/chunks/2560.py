def test_sync_sync_raise_raises():
    with pytest.raises(SyncDependencyError):
        client.get("/sync_sync_raise")
    assert state["/sync_raise"] == "generator raise finalized"
    assert "/sync_raise" in errors
    errors.clear()