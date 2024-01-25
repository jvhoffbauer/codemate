@pytest.fixture(autouse=True)
def _setup_sync_db() -> Database:
    yield sync_db
    # Free connection pool resources
    sync_db.close()  # type: ignore