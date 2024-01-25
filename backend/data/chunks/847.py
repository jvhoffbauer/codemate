    def client(self):
        return httpx.AsyncClient(base_url=self.BASE_URL, timeout=10.0)