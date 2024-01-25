def test_MosaicTilerFactory_PixelSelectionParams():
    """Test MosaicTilerFactory factory with a customized default PixelSelectionMethod."""
    mosaic = MosaicTilerFactory(router_prefix="/mosaic")
    mosaic_highest = MosaicTilerFactory(
        pixel_selection_dependency=lambda: PixelSelectionMethod.highest.method(),
        router_prefix="/mosaic_highest",
    )

    app = FastAPI()
    app.include_router(mosaic.router, prefix="/mosaic")
    app.include_router(mosaic_highest.router, prefix="/mosaic_highest")
    client = TestClient(app)

    with tmpmosaic() as mosaic_file:
        response = client.get("/mosaic/tiles/7/37/45.npy", params={"url": mosaic_file})
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/x-binary"
        npy_tile = numpy.load(BytesIO(response.content))
        assert npy_tile.shape == (4, 256, 256)  # mask + data

        response = client.get(
            "/mosaic_highest/tiles/7/37/45.npy", params={"url": mosaic_file}
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/x-binary"
        npy_tile_highest = numpy.load(BytesIO(response.content))
        assert npy_tile_highest.shape == (4, 256, 256)  # mask + data

        assert (npy_tile != npy_tile_highest).any()