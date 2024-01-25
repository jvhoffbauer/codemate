async def test_schema_update_relationship(
    app: FastAPI, async_client: AsyncClient, fake_articles, async_session, models
):
    content_schema = TableModelParser.get_table_model_schema(models.ArticleContent)

    class ArticleUpdate(BaseModel):
        title: str = None
        description: str = None
        content: Optional[content_schema] = None  # Relationship

    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        update_exclude = {"content": {"id"}}
        schema_update = ArticleUpdate

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]

    assert "content" in schemas["ArticleUpdate"]["properties"]
    # assert schemas["ArticleUpdate"]["properties"]["content"]["$ref"] == "#/components/schemas/" + content_schema.__name__

    # test api
    res = await async_client.put("/article/item/1", json={"title": "new_title"})
    assert res.json()["data"] == 1
    article = await async_session.get(models.Article, 1, with_for_update=True)
    await async_session.refresh(article)
    assert article.title == "new_title"

    res = await async_client.put(
        "/article/item/1",
        json={
            "content": {"id": 2, "content": "new_content"}
        },  # will be ignored by `update_exclude`
    )
    assert res.json()["data"] == 1
    content = await async_session.get(models.ArticleContent, 1, with_for_update=True)
    await async_session.refresh(content)
    assert content.content == "new_content"