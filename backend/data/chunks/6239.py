def client(site: AdminSite) -> TestClient:
    with TestClient(app=site.fastapi, base_url="http://testserver") as c:
        yield c