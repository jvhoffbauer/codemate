@pytest.fixture
async def fake_article_tags(async_session, fake_articles, models) -> List[Tag]:
    # add tags
    data = [models.Tag(id=i, name=f"Tag_{i}") for i in range(1, 6)]
    async_session.add_all(data)
    await async_session.commit()
    # add article_tag_link
    async_session.add_all(
        [models.ArticleTagLink(article_id=i, tag_id=i) for i in range(1, 6)]
    )
    await async_session.commit()
    return data