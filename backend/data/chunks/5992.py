    def site(self) -> "BaseAdminSite":
        return self if self.app is self else self.app.site