    def __init__(self, app: "AdminApp"):
        assert self.templates, "templates:Jinja2Templates is None"
        assert self.template_name, "template_name is None"
        self.page_path = self.page_path or f"/{self.template_name}"
        super().__init__(app)