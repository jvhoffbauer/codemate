    @cached_property
    def router_path(self) -> str:
        return self.settings.site_url + self.settings.site_path + self.router.prefix