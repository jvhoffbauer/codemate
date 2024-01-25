    async def test_root_api(self):
        """Validate that / returns a 200 and is not a redirect."""
        response = await self.asgi_client.get("/")

        assert response.status_code == 200
        assert not response.is_redirect