async def test_fields(models):
    class ArticleSelector(SqlalchemySelector):
        router_prefix = "/user"
        fields = [
            "id",
            models.Article.title,
            models.User.username,
            models.User.password.label("pwd"),
            "not_exist",
        ]

    selector = ArticleSelector(models.Article)
    assert "id" in selector._select_entities
    assert "title" in selector._select_entities
    assert "user__username" in selector._select_entities
    assert "pwd" in selector._select_entities
    assert "not_exist" not in selector._select_entities
    assert selector._filter_entities == selector._select_entities