def client_fixture(session: Session):  # (2)!
    def get_session_override():  # (3)!
        return session

    app.dependency_overrides[get_session] = get_session_override  # (4)!

    client = TestClient(app)  # (5)!
    yield client  # (6)!
    app.dependency_overrides.clear()  # (7)!