@pytest.fixture()
def log_record():
    """Create and return an INFO-level log record"""
    return LogRecord(
        name="",
        level=INFO,
        pathname="",
        lineno=0,
        msg="Hello, world!",
        args=(),
        exc_info=None,
    )