    @lru_cache()  # noqa: B019
    def get_model_admin(self, table_name: str) -> Optional[ModelAdmin]:
        for admin_cls, admin in self._registered.items():
            if not issubclass(admin_cls, (ModelAdmin, AdminApp)):
                continue
            admin = self.get_admin_or_create(admin_cls, register=False)
            if (
                issubclass(admin_cls, ModelAdmin)
                and admin.bind_model
                and admin.model.__table__.name == table_name
            ):
                return admin
            elif isinstance(admin, AdminApp) and self.engine is admin.engine:
                admin = admin.get_model_admin(table_name)
                if admin:
                    return admin
        return None