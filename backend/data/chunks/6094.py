    def _get_admin_or_create_nested(
        self,
        admin_cls: Type[BaseAdminT],
    ) -> Optional[BaseAdminT]:
        """Get or create admin instance in nested app"""
        if admin_cls in self._registered:
            return self.get_admin_or_create(admin_cls, register=False, nested=False)
        for app_cls, app in self._registered.items():
            if not issubclass(app_cls, AdminApp):
                continue
            app = self.get_admin_or_create(app_cls, register=False, nested=False)
            if app is None:
                continue
            admin = app._get_admin_or_create_nested(admin_cls)
            if admin:
                return admin
        return None