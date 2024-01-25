def test_read_model_no_alias():
    response = client.get("/no-alias/model")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo"}