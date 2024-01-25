def test_incorrect_multipart_installed_form_file(monkeypatch):
    monkeypatch.delattr("multipart.multipart.parse_options_header", raising=False)
    with pytest.raises(RuntimeError, match=multipart_incorrect_install_error):
        app = FastAPI()

        @app.post("/")
        async def root(username: str = Form(), f: UploadFile = File()):
            return username  # pragma: nocover