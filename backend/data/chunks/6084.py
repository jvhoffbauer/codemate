    def __init__(self, app: "AdminApp") -> None:
        super().__init__(app)
        self._children: List[PageSchemaAdminT] = []