    def _register_admin_router_all_pre(self):
        [
            admin.get_link_model_forms()
            for admin in self._registered.values()
            if isinstance(admin, ModelAdmin)
        ]