async def test_user_count(session: AsyncSession, user):
    adal = AsyncDal(session)
    assert len(await adal.all(User)) == 1