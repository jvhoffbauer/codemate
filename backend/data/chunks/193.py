def get_session():
    with Session(engine) as session:
        yield session