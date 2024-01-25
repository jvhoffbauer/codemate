def test_sync_context_b_raise():
    with pytest.raises(OtherDependencyError):
        client.get("/sync_context_b_raise")
    assert state["context_b"] == "finished b with a: started a"
    assert state["context_a"] == "finished a"