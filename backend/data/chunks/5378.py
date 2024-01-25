def test_cogValidateExtension():
    """Test cogValidateExtension class."""
    tiler = TilerFactory()
    tiler_plus_cog = TilerFactory(extensions=[cogValidateExtension()])
    # Check that we added one route (/validate)
    assert len(tiler_plus_cog.router.routes) == len(tiler.router.routes) + 1

    app = FastAPI()
    app.include_router(tiler_plus_cog.router)
    with TestClient(app) as client:
        response = client.get("/validate", params={"url": cog})
        assert response.status_code == 200
        body = response.json()
        assert body["COG"]