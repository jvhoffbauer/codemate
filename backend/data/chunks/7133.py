@pytest.fixture(scope="session")
def db() -> Generator:
    with Session(engine) as session:
        yield session