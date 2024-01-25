async def test_schema_read_relationship(
    app: FastAPI, async_client: AsyncClient, fake_articles, fake_article_tags, models
):
    category_schema = TableModelParser.get_table_model_schema(models.Category)
    content_schema = TableModelParser.get_table_model_schema(models.ArticleContent)
    user_schema = TableModelParser.get_table_model_schema(models.User)
    tag_schema = TableModelParser.get_table_model_schema(models.Tag)

    class ArticleRead(ORMModelMixin):
        id: int
        title: str
        description: str
        category: Optional[category_schema] = None  # Relationship
        content: Optional[content_schema] = None  # Relationship
        user: Optional[user_schema] = None  # Relationship
        tags: List[tag_schema] = []  # Relationship

    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"
        schema_read = ArticleRead

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)

    # test schemas
    openapi = app.openapi()
    schemas = openapi["components"]["schemas"]
    assert "category" in schemas["ArticleRead"]["properties"]
    # assert schemas["ArticleRead"]["properties"]["category"]["$ref"] == "#/components/schemas/" + category_schema.__name__
    assert "content" in schemas["ArticleRead"]["properties"]
    assert "user" in schemas["ArticleRead"]["properties"]
    assert "tags" in schemas["ArticleRead"]["properties"]

    # test api
    res = await async_client.get("/article/item/1")
    items = res.json()["data"]
    assert items["id"] == 1
    assert "category" in items
    assert "content" in items
    assert "user" in items
    assert items["category"]["id"] == 1
    assert items["content"]["id"] == 1
    assert items["user"]["id"] == 1
    assert items["tags"][0]["id"] == 1