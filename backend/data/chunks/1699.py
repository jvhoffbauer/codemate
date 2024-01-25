def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()