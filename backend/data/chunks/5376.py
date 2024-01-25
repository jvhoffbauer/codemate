def test_cogViewerExtension():
    """Test cogViewerExtension class."""
    tiler = TilerFactory()
    tiler_plus_viewer = TilerFactory(extensions=[cogViewerExtension()])
    assert len(tiler_plus_viewer.router.routes) == len(tiler.router.routes) + 1

    app = FastAPI()
    app.include_router(tiler_plus_viewer.router)
    with TestClient(app) as client:
        response = client.get("/viewer")
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"