async def test_staff_count(session: AsyncSession, staff):
    adal = AsyncDal(session)
    assert len(await adal.all(Staff)) == 1