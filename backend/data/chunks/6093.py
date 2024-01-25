    def get_admin_or_create(
        self,
        admin_cls: Type[BaseAdminT],
        *,
        register: bool = True,
        nested: bool = True,
    ) -> Optional[BaseAdminT]:
        """Get or create admin instance"""
        admin = self._registered.get(admin_cls, None)
        if admin is None and nested:
            admin = self._get_admin_or_create_nested(admin_cls)
        if admin:
            return admin
        if not register or self.__register_lock:
            return None
        # create admin instance
        admin = admin_cls(self)
        self._registered[admin_cls] = admin
        if isinstance(admin, PageSchemaAdmin):
            self.append_child(admin)
        return admin