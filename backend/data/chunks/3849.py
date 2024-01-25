@pytest.fixture(scope="module")
def client():
    test_db = Path("./sql_app.db")
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()
    # Import while creating the client to create the DB after starting the test session
    from docs_src.sql_databases.sql_app import alt_main

    # Ensure import side effects are re-executed
    importlib.reload(alt_main)

    with TestClient(alt_main.app) as c:
        yield c
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()