    def register_router(self):
        for admin_action in self.registered_admin_actions.values():
            if isinstance(admin_action, RouterAdmin):
                admin_action.register_router()
        return super().register_router()