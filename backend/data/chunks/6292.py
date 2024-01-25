def admin_cls_list(models) -> Tuple[Type[admin.ModelAdmin], Type[admin.AdminApp]]:
    class UserAdmin(admin.ModelAdmin):
        model = models.User

    class BlogApp(admin.AdminApp):
        def __init__(self, app: "AdminApp"):
            super().__init__(app)
            self.register_admin(UserAdmin)

    return UserAdmin, BlogApp