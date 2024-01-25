def test_read_dict_by_alias():
    response = client.get("/by-alias/dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"alias": "Foo"}