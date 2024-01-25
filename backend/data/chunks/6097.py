    def _register_admin_router_all(self):
        for admin in self._registered.values():
            if isinstance(admin, RouterAdmin):  # register route
                admin.register_router()
                self.router.include_router(admin.router)