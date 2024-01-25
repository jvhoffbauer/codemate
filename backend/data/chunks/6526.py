def api_client():
    """
    Returns a fastapi.testclient.TestClient.
    The test client uses the requests library for making http requests.
    """
    return TestClient(APP)