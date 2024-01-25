def test_read_list_by_alias():
    response = client.get("/by-alias/list")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"alias": "Foo"},
        {"alias": "Bar"},
    ]