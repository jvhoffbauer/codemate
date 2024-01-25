@pytest.fixture
async def fake_categorys(async_session, models) -> List[Category]:
    data = [models.Category(id=i, name=f"Category_{i}") for i in range(1, 6)]
    async_session.add_all(data)
    await async_session.commit()
    return data