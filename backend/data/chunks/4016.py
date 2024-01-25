@needs_py310
def test_post_body_q_bar_content(client: TestClient):
    response = client.put("/items/5?q=bar", json={"name": "Foo", "price": 50.5})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 5,
        "item": {
            "name": "Foo",
            "price": 50.5,
            "description": None,
            "tax": None,
        },
        "q": "bar",
    }