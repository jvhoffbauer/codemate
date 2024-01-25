async def test_delete_current_user(
    client: AsyncClient, default_user_headers, session: AsyncSession
):
    response = await client.delete(
        app.url_path_for("delete_current_user"), headers=default_user_headers
    )
    assert response.status_code == codes.NO_CONTENT
    result = await session.execute(select(User).where(User.id == default_user_id))
    user = result.scalars().first()
    assert user is None