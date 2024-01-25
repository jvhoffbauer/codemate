    def __init__(self, app: "AdminApp"):
        RouterAdmin.__init__(self, app)
        if self.page_path is None:
            self.page_path = f"/{self.__class__.__module__}/{self.__class__.__name__}"
        PageSchemaAdmin.__init__(self, app)