def test_no_token():
    response = client.get("/items")
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}