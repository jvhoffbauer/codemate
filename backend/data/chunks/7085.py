def get_db() -> Generator:
    with Session(engine) as session:
        yield session