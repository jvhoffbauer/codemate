def get_app():
    with pytest.warns(DeprecationWarning):
        from docs_src.async_sql_databases.tutorial001 import app
    yield app