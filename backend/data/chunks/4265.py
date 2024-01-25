@pytest.fixture(name="app")
def get_app():
    from docs_src.websockets.tutorial003_py39 import app

    return app