def test_create_item(superuser_token_headers):
    server_api = get_server_api()
    data = {"title": "Foo", "description": "Fighters"}
    response = requests.post(
        f"{server_api}{config.API_V1_STR}/items/",
        headers=superuser_token_headers,
        json=data,
    )
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_username" in content