async def test_list_filter(models):
    class ArticleSelector(SqlalchemySelector):
        router_prefix = "/user"
        list_filter = [
            "id",
            models.Article.title,
            models.User.username,
            models.User.password.label("pwd"),
            "not_exist",
        ]

    selector = ArticleSelector(models.Article)
    assert "id" in selector._filter_entities
    assert "title" in selector._filter_entities
    assert "user__username" in selector._filter_entities
    assert "pwd" in selector._filter_entities
    assert "not_exist" not in selector._filter_entities
    assert selector._filter_entities != selector._select_entities