    def unregister_admin(self, *admin_cls: Type[BaseAdmin]):
        [self._registered.pop(cls) for cls in admin_cls if cls in self._registered]