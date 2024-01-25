def test_no_multipart_installed_form_file(monkeypatch):
    monkeypatch.delattr("multipart.__version__", raising=False)
    with pytest.raises(RuntimeError, match=multipart_not_installed_error):
        app = FastAPI()

        @app.post("/")
        async def root(username: str = Form(), f: UploadFile = File()):
            return username  # pragma: nocover