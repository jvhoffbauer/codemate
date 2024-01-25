    def _create_admin_instance_all(self) -> None:
        [self.get_admin_or_create(admin_cls) for admin_cls in self._registered.keys()]