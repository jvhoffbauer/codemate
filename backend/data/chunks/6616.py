    @computed_field
    @cached_property
    def TEST_SQLALCHEMY_DATABASE_URI(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=self.TEST_DATABASE_USER,
                password=self.TEST_DATABASE_PASSWORD,
                host=self.TEST_DATABASE_HOSTNAME,
                port=self.TEST_DATABASE_PORT,
                path=self.TEST_DATABASE_DB,
            )
        )