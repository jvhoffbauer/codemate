async def test_update_fields_relationship(
    app: FastAPI, async_client: AsyncClient, fake_articles, async_session, models
):
    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        update_exclude = {"content": {"id"}}
        update_fields = [
            models.Article.description,
            PropertyField(
                name="content", type_=ArticleContentSchema
            ),  # Relationship attribute
        ]
        read_fields = [
            models.Article.title,
            models.Article.description,
            PropertyField(
                name="content", type_=ArticleContentSchema
            ),  # Relationship attribute
        ]

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    assert "id" not in model_fields(ins.schema_update)
    assert "title" not in model_fields(ins.schema_update)
    assert "description" in model_fields(ins.schema_update)
    assert "content" in model_fields(ins.schema_update)

    # test api
    res = await async_client.put(
        "/article/item/1",
        json={
            "title": "new_title",
            "description": "new_description",
            "content": {
                "id": 22,  # will be ignored by `update_exclude`
                "content": "new_content",
            },
        },
    )
    assert res.json()["data"] == 1

    article = await async_session.get(models.Article, 1)
    await async_session.refresh(article)

    assert article.title != "new_title"
    assert article.description == "new_description"

    content = await async_session.get(models.ArticleContent, 1)
    await async_session.refresh(content)
    assert content.content == "new_content"