def test_post_a():
    data = {"a": 2, "b": "foo"}
    response = client.post("/a/compute", json=data)
    assert response.status_code == 200, response.text
    data = response.json()