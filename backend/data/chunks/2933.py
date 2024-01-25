def test_incorrect_multipart_installed_file_upload(monkeypatch):
    monkeypatch.delattr("multipart.multipart.parse_options_header", raising=False)
    with pytest.raises(RuntimeError, match=multipart_incorrect_install_error):
        app = FastAPI()

        @app.post("/")
        async def root(f: UploadFile = File()):
            return f  # pragma: nocover