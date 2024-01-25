@pytest.fixture
async def fake_articles(
    async_session, fake_users, fake_categorys, fake_article_contents, models
) -> List[Article]:
    data = [
        models.Article(
            id=i,
            title=f"Article_{i}",
            description=f"Description_{i}",
            user_id=i,
            category_id=i,
            content_id=i,
        )
        for i in range(1, 6)
    ]
    async_session.add_all(data)
    await async_session.commit()
    return data