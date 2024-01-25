    def setUp(self):
        self.asgi_client = TestClient(APP)
        self.date = DATETIME_STRING