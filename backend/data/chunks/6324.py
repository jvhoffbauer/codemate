    @site.register_admin
    class ArticleAdmin(admin.ModelAdmin):
        model = models.Article
        list_display = [
            models.Article.title,
            models.User.username,
            "description",
            models.User.username.label("nickname"),
            LabelField(
                label=models.User.password.label("pwd"),
                field=Field(None, title="pwd_title"),
            ),
        ]

        async def get_select(self, request: Request) -> Select:
            sel = await super().get_select(request)
            return sel.outerjoin(models.User, models.User.id == models.Article.user_id)