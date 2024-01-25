    @property
    def src(self):
        return self.app.site.router_path + self.app.site.fastapi.redoc_url