    def __init__(
        self,
        app: ASGIApp,
        querystrings: bool = False,
        headers: bool = False,
    ) -> None:
        """Init Middleware.

        Args:
            app (ASGIApp): starlette/FastAPI application.

        """
        self.app = app
        self.querystrings = querystrings
        self.headers = headers
        self.logger = logger
        logger.setLevel(logging.DEBUG)