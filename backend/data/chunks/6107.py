    def __init__(
        self,
        settings: Settings,
        *,
        fastapi: FastAPI = None,
        engine: SqlalchemyDatabase = None,
    ):
        self.application = None
        try:
            from fastapi_user_auth.auth import Auth

            self.auth: Auth = None  # type: ignore
        except ImportError:
            pass
        self.settings = settings
        self.amis_parser = AmisParser(
            image_receiver=self.settings.amis_image_receiver,
            file_receiver=self.settings.amis_file_receiver,
        )
        kwargs = (
            {
                "debug": True,
            }
            if settings.debug
            else {
                "openapi_url": None,
                "docs_url": None,
                "redoc_url": None,
            }
        )

        self.fastapi = fastapi or FastAPI(**kwargs)
        self.router = self.fastapi.router
        if engine:
            self.engine = engine
        elif settings.database_url_async:
            self.engine = AsyncDatabase.create(
                settings.database_url_async, echo=settings.debug
            )
        elif settings.database_url:
            self.engine = Database.create(settings.database_url, echo=settings.debug)
        super().__init__(self)