async def async_client(site: AdminSite) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=site.fastapi, base_url="http://testserver") as c:
        yield c