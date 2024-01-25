def test_MosaicTilerFactory_strict_zoom(monkeypatch):
    """Test MosaicTilerFactory factory with STRICT Zoom Mode"""
    monkeypatch.setenv("MOSAIC_STRICT_ZOOM", True)

    mosaic = MosaicTilerFactory()
    app = FastAPI()
    app.include_router(mosaic.router)

    with TestClient(app) as client:
        with tmpmosaic() as mosaic_file:
            response = client.get("/tiles/7/37/45.png", params={"url": mosaic_file})
            assert response.status_code == 200

            response = client.get("/tiles/6/18/22.png", params={"url": mosaic_file})
            assert response.status_code == 400
            assert "Invalid ZOOM level 6" in response.text

            response = client.get("/tiles/11/594/734.png", params={"url": mosaic_file})
            assert response.status_code == 400
            assert "Invalid ZOOM level 11" in response.text