def client(tmp_path_factory: pytest.TempPathFactory):
    tmp_path = tmp_path_factory.mktemp("data")
    cwd = os.getcwd()
    os.chdir(tmp_path)
    test_db = Path("./sql_app.db")
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()
    # Import while creating the client to create the DB after starting the test session
    from docs_src.sql_databases.sql_app import main

    # Ensure import side effects are re-executed
    importlib.reload(main)
    with TestClient(main.app) as c:
        yield c
    if test_db.is_file():  # pragma: nocover
        test_db.unlink()
    os.chdir(cwd)