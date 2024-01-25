async def test_register_new_user(
    client: AsyncClient, default_user_headers, session: AsyncSession
):
    response = await client.post(
        app.url_path_for("register_new_user"),
        headers=default_user_headers,
        json={
            "email": "qwe@example.com",
            "password": "asdasdasd",
        },
    )
    assert response.status_code == codes.OK
    result = await session.execute(select(User).where(User.email == "qwe@example.com"))
    user = result.scalars().first()
    assert user is not None