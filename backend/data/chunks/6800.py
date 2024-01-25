@pytest.fixture
def assert_log_errors(caplog):
    def _assert_log_errors(*errors):
        error_messages = []
        error_raises = []
        for error in errors:
            if isinstance(error, str):
                error_messages.append(error)
                error_raises.append(None)
            else:
                assert isinstance(
                    error, RaisesContext
                ), "errors-element must be string or pytest.raises(...)"
                assert error_raises[-1] is None
                error_raises[-1] = error

        error_records = [r for r in caplog.records if r.levelno >= logging.ERROR]

        assert [r.message for r in error_records] == error_messages

        for record, error_raises_ctx in zip(error_records, error_raises):
            if error_raises_ctx is not None:
                with error_raises_ctx:
                    raise record.exc_info[1]

        # clear caplog records
        for when in ("setup", "call"):
            del caplog.get_records(when)[:]
        caplog.clear()

    return _assert_log_errors