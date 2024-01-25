@asynccontextmanager
async def mocked_session_get(*args, **kwargs):
    """Mock response from client_session.get."""

    url = args[0]
    filename = url.split("/")[-1]

    # clean up for id token (e.g. Deaths)
    state = filename.split("-")[-1].replace(".csv", "").lower().capitalize()

    yield FakeRequestsGetResponse(url, filename, state)