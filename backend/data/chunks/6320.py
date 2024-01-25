    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        model = models.User