    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        self.page_schema = self.get_page_schema()
        if self.page_schema and self.page_schema.url:
            self.page_schema.url = self.page_schema.url.replace(
                self.site.settings.site_url, ""
            )