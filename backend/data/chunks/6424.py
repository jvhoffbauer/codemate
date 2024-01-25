async def test_read_fields_and_schema_read_is_none(app: FastAPI, models):
    class ArticleCrud(SqlalchemyCrud):
        router_prefix = "/article"

    ins = ArticleCrud(models.Article, db.engine).register_crud()

    app.include_router(ins.router)
    assert ins.schema_read is None

    with pytest.raises(NoMatchFound):
        ins.router.url_path_for("read")

    # test schemas
    openapi = app.openapi()
    paths = openapi["paths"]
    assert "/article/list" in paths
    assert "/article/item/{item_id}" in paths
    assert "put" in paths["/article/item/{item_id}"]
    assert "get" not in paths["/article/item/{item_id}"]