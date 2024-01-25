    def register_admin(self, *admin_cls: Type[BaseAdminT]) -> Type[BaseAdminT]:
        [self._registered.update({cls: None}) for cls in admin_cls if cls]
        return admin_cls[0]