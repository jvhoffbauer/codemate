    def __init__(self, app: "AdminApp"):
        BaseAdmin.__init__(self, app)
        RouterMixin.__init__(self)