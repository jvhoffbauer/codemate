@needs_py39
def test_read_items(client: TestClient):
    access_token = get_access_token(scope="me items", client=client)
    response = client.get(
        "/users/me/items/", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == [{"item_id": "Foo", "owner": "johndoe"}]