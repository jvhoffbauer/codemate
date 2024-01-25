@pytest.fixture
async def fake_article_contents(async_session, models) -> List[ArticleContent]:
    data = [models.ArticleContent(id=i, content=f"Content_{i}") for i in range(1, 6)]
    async_session.add_all(data)
    await async_session.commit()
    return data