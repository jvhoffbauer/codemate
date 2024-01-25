def test_sync_context_b():
    response = client.get("/sync_context_b")
    data = response.json()
    assert data["context_b"] == "started b"
    assert data["context_a"] == "started a"
    assert state["context_b"] == "finished b with a: started a"
    assert state["context_a"] == "finished a"