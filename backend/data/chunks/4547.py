def get_app():
    with pytest.warns(DeprecationWarning):
        from docs_src.events.tutorial001 import app
    yield app