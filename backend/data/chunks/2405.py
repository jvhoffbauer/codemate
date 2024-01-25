def test_incorrect_token():
    response = client.get("/items", headers={"Authorization": "Notexistent testtoken"})
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}