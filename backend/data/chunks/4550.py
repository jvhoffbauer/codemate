@pytest.fixture(name="app", scope="module")
def get_app():
    with pytest.warns(DeprecationWarning):
        from docs_src.events.tutorial002 import app
    yield app