def test_no_multipart_installed_file_bytes(monkeypatch):
    monkeypatch.delattr("multipart.__version__", raising=False)
    with pytest.raises(RuntimeError, match=multipart_not_installed_error):
        app = FastAPI()

        @app.post("/")
        async def root(f: bytes = File()):
            return f  # pragma: nocover