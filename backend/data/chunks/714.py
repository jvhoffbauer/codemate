    def __init__(
        self,
        name: str = "",
        uuid_length: Optional[int] = None,
        default_value: Optional[str] = None,
    ):
        super().__init__(name=name)
        self.uuid_length = uuid_length
        self.default_value = default_value