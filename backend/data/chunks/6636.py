async def test_reset_current_user_password(
    client: AsyncClient, default_user_headers, session: AsyncSession
):
    response = await client.post(
        app.url_path_for("reset_current_user_password"),
        headers=default_user_headers,
        json={"password": "testxxxxxx"},
    )
    assert response.status_code == codes.OK
    result = await session.execute(select(User).where(User.id == default_user_id))
    user = result.scalars().first()
    assert user is not None
    assert user.hashed_password != default_user_password_hash