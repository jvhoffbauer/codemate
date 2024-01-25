def client():
    static_dir: Path = Path(os.getcwd()) / "static"
    print(static_dir)
    static_dir.mkdir(exist_ok=True)
    from docs_src.custom_docs_ui.tutorial002 import app

    with TestClient(app) as client:
        yield client
    static_dir.rmdir()