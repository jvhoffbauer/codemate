def test_sync_background_tasks():
    response = client.get("/sync_context_b_bg")
    data = response.json()
    assert data["context_b"] == "started b"
    assert data["context_a"] == "started a"
    assert data["sync_bg"] == "not set"
    assert state["context_b"] == "finished b with a: started a"
    assert state["context_a"] == "finished a"
    assert state["sync_bg"] == "sync_bg set - b: started b - a: started a"