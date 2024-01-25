    def __init__(self, request: Request):
        super().__init__(scope=ChainMap({}, request.scope))
        self.request = request