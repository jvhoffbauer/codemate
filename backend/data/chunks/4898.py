@pytest.fixture(name="app")
def get_app():
    from docs_src.request_forms_and_files.tutorial001_an_py39 import app

    return app