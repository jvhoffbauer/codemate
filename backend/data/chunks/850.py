async def get_public_apis() -> PublicAPIsResponse:
    cg_client = Client()

    return await cg_client.get_public_apis()