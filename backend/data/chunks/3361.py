def test_read_dict():
    response = client.get("/dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo"}