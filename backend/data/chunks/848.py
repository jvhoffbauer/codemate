    async def get_public_apis(self) -> PublicAPIsResponse:
        async with self.client as client:
            response = await client.get("/entries")

            return PublicAPIsResponse.model_validate_json(response.read())