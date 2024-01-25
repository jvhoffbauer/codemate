def mock_RequestGet(src_path):
    """Mock Requests."""

    # HTTP
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return json.loads(self.data)

        def raise_for_status(self):
            return True

    assert src_path.startswith("https://myurl.com/")
    stac_path = os.path.basename(src_path)
    with open(os.path.join(DATA_DIR, stac_path), "r") as f:
        return MockResponse(f.read())