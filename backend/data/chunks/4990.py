def test_post_b_invalid():
    data = {"a": "bar", "b": "foo"}
    response = client.post("/b/compute/", json=data)
    assert response.status_code == 422, response.text