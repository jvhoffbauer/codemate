async def test_read_current_user(client: AsyncClient, default_user_headers):
    response = await client.get(
        app.url_path_for("read_current_user"), headers=default_user_headers
    )
    assert response.status_code == codes.OK
    assert response.json() == {
        "id": default_user_id,
        "email": default_user_email,
    }