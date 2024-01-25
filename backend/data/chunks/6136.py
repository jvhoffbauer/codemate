    def __init__(
        self,
        settings: Settings,
        *,
        fastapi: FastAPI = None,
        engine: SqlalchemyDatabase = None,
    ):
        super().__init__(settings, fastapi=fastapi, engine=engine)
        self.register_admin(
            HomeAdmin,
            APIDocsApp,
            FileAdmin,
        )