- Defines a fixture named `test_db_setup_sessionmaker` that is scoped to the entire PyTest session using `@pytest_asyncio.fixture`.
- Asserts that the environment variable `config.settings.ENVIRONMENT` equals 'PYTEST' before proceeding, ensuring that this setup is used exclusively during testing.
- Drops all existing database tables in the test database using SQLAlchemy's `DropAll` method within an `AsyncEngine` connection context manager (`conn`) created by `async_engine`, then creates them again using `CreateAll`. This ensures that each test runs against a clean slate of data.