def test_post_a_invalid():
    data = {"a": "bar", "b": "foo"}
    response = client.post("/a/compute", json=data)
    assert response.status_code == 422, response.text