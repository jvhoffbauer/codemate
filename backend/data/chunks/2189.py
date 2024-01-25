def test_call_invalid():
    response = client.post("/", json={"foo": {"bar": "baz"}})
    assert response.status_code == 422