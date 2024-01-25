def test_read_model_by_alias():
    response = client.get("/by-alias/model")
    assert response.status_code == 200, response.text
    assert response.json() == {"alias": "Foo"}