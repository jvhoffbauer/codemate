def mock_client_session_class(request):
    """Class fixture to expose an AsyncMock to unittest.TestCase subclasses.

    See: https://docs.pytest.org/en/5.4.1/unittest.html#mixing-pytest-fixtures-into-unittest-testcase-subclasses-using-marks
    """

    httputils.CLIENT_SESSION = request.cls.mock_client_session = AsyncMock()
    httputils.CLIENT_SESSION.get = mocked_session_get
    try:
        yield
    finally:
        del httputils.CLIENT_SESSION