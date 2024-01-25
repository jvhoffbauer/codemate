async def test_read_fields(
    app: FastAPI, async_client: AsyncClient, fake_articles, models
):
    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        read_fields = [
            models.Article.title,
            models.Article.description,
            # Article.category,  # Relationship
            # Article.user  # Relationship
        ]

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    assert "id" not in model_fields(ins.schema_read)
    assert "title" in model_fields(ins.schema_read)
    assert "description" in model_fields(ins.schema_read)
    # test api
    res = await async_client.get("/article/item/1")
    items = res.json()["data"]
    assert "id" not in items
    assert items["title"] == "Article_1"
    assert items["description"] == "Description_1"