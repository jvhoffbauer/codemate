@needs_py310
def test_post_no_body_q_bar(client: TestClient):
    response = client.put("/items/5?q=bar", json=None)
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "bar"}