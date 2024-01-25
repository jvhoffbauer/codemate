@pytest.fixture(scope="session")
async def user(session: AsyncSession):
    adal = AsyncDal(session)
    ins = adal.add(
        User,
        email="alphago@gmail.com",
        is_active=True,
        password="plain_password",
        last_login_at=datetime.datetime.now(),
        first_name="alpha",
        last_name="go",
    )
    await adal.commit()
    return ins