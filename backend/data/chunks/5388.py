    def __init__(self, app: ASGIApp) -> None:
        """Init Middleware.

        Args:
            app (ASGIApp): starlette/FastAPI application.

        """
        self.app = app