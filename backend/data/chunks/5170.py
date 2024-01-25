def test_read_item(superuser_token_headers):
    item = create_random_item()
    server_api = get_server_api()
    response = requests.get(
        f"{server_api}{config.API_V1_STR}/items/{item.id}",
        headers=superuser_token_headers,
    )
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
    assert content["owner_username"] == item.owner_username