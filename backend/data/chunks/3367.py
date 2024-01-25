def test_read_dict_no_alias():
    response = client.get("/no-alias/dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo"}