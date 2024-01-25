    def __init__(
        self,
        content: typing.Any,
        status_code: int = 200,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        media_type: typing.Optional[str] = None,
        background: typing.Optional[BackgroundTask] = None,
        exc: Exception = None,
    ) -> None:
        self.exc = exc
        super().__init__(content, status_code, headers, media_type, background)