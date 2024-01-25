def db() -> Generator:
    yield SessionLocal()