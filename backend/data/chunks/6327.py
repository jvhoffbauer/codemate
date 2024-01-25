    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User
        list_filter = [models.User.id, models.User.username.label("name")]
        search_fields = [models.User.username]