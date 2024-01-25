    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User
        list_display = [models.User.id, models.User.username]