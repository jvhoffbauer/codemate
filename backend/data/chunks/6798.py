@pytest.fixture(autouse=True)
def check_no_errors(caplog):
    yield
    for when in ("setup", "call"):
        messages = [
            x.message for x in caplog.get_records(when) if x.levelno >= logging.ERROR
        ]
        if messages:
            pytest.fail(f"error messages encountered during testing: {messages!r}")