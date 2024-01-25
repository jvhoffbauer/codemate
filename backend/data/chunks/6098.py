    def register_router(self):
        if not self.__register_lock:
            super(AdminApp, self).register_router()
            self._create_admin_instance_all()
            self._register_admin_router_all_pre()
            self._register_admin_router_all()
            self.__register_lock = True
        return self