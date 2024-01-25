def test_read_list():
    response = client.get("/list")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"name": "Foo"},
        {"name": "Bar"},
    ]