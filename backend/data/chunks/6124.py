    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        if self.app.site.fastapi.docs_url:
            self.register_admin(DocsAdmin)
        if self.app.site.fastapi.redoc_url:
            self.register_admin(ReDocsAdmin)