@pytest.fixture(name="app")
def get_app():
    from docs_src.request_forms_and_files.tutorial001_an import app

    return app