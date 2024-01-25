def test_read_list_no_alias():
    response = client.get("/no-alias/list")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"name": "Foo"},
        {"name": "Bar"},
    ]