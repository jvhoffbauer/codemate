def db() -> Generator:
    db = SessionLocal()
    init_db(db)
    yield db
    db.close()