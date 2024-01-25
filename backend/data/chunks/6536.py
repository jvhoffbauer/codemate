@pytest.fixture
async def mock_client_session():
    """Context manager fixture that replaces the global client_session with an AsyncMock
    instance.
    """

    httputils.CLIENT_SESSION = AsyncMock()
    httputils.CLIENT_SESSION.get = mocked_session_get
    try:
        yield httputils.CLIENT_SESSION
    finally:
        del httputils.CLIENT_SESSION