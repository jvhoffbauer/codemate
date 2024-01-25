def session():
    with sync_db.session_maker() as session:
        yield session