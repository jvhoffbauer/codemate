    @cached_property
    def router_path(self) -> str:
        if self.router is self.app.router:
            return self.app.router_path
        return self.app.router_path + self.router.prefix