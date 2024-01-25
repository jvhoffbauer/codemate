async def test_read_fields_relationship(
    app: FastAPI, async_client: AsyncClient, fake_articles, fake_article_tags, models
):
    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        read_fields = [
            models.Article.title,
            models.Article.description,
            PropertyField(
                name="category", type_=CategorySchema
            ),  # Relationship attribute
            # Article.category,  # Relationship todo support
            PropertyField(name="content_text", type_=str),  # property attribute
            PropertyField(name="tags", type_=List[TagSchema]),  # property attribute
        ]

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    assert "id" not in model_fields(ins.schema_read)
    assert "title" in model_fields(ins.schema_read)
    assert "description" in model_fields(ins.schema_read)
    assert "category" in model_fields(ins.schema_read)
    assert "tags" in model_fields(ins.schema_read)
    # test api
    res = await async_client.get("/article/item/1")
    items = res.json()["data"]
    assert "id" not in items
    assert "category" in items
    assert items["category"]["name"] == "Category_1"
    assert "content_text" in items
    assert items["tags"][0]["name"] == "Tag_1"