    @property
    def router_prefix(self):
        if issubclass(self.__class__.__base__, ModelAdmin):
            return f"/{self.__class__.__name__}"
        return f"/{self.model.__name__}"