def test_get():
    response = client.get("/seg/users/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"segment": "seg", "id": "foo"}