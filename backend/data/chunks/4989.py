def test_post_b():
    data = {"a": 2, "b": "foo"}
    response = client.post("/b/compute/", json=data)
    assert response.status_code == 200, response.text
    data = response.json()