@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()