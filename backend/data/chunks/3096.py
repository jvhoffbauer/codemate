def test_post_other_item():
    response = client.post("/items/", json={"price": 100})
    assert response.status_code == 200, response.text
    assert response.json() == {"item": {"price": 100}}