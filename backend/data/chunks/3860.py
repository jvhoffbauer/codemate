@needs_py39
# TODO: pv2 add version with Pydantic v2
@needs_pydanticv1
def test_create_user(client):
    test_user = {"email": "johndoe@example.com", "password": "secret"}
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200, response.text
    data = response.json()
    assert test_user["email"] == data["email"]
    assert "id" in data
    response = client.post("/users/", json=test_user)
    assert response.status_code == 400, response.text