async def async_api_client():
    """
    Returns an async_asgi_testclient.TestClient.
    """
    return AsyncTestClient(APP)