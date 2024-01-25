    @site.register_admin
    class ArticleAdmin(admin.BaseAuthFieldModelAdmin):
        model = models.Article
        read_fields = [
            models.Article.id,
            models.Article.title,
            models.Article.description,
            models.Article.status,
            models.Article.category_id,
        ]
        perm_fields_exclude = {
            FieldPermEnum.VIEW: ["id", "title"],
            FieldPermEnum.UPDATE: ["status"],
            FieldPermEnum.CREATE: ["description", "status"],
        }