def test_read_item(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    item = create_random_item(db)
    response = client.get(
        f"{settings.API_STR}{settings.API_V1_STR}/items/{item.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == item.id
    assert content["owner_id"] == item.owner_id