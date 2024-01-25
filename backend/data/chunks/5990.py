    def __init__(self, app: "AdminApp"):
        self.app = app
        assert self.app, "app is None"