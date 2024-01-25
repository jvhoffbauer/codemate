    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        assert self.schema, "schema is None"
        self.form_path = self.form_path or f"{self.page_path}/api"