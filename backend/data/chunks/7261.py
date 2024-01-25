async def override_dependency(session: AsyncSession):
    app.dependency_overrides[get_session] = lambda: session