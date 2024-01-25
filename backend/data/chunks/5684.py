def test_AutoFormat_Colormap():
    """Make sure we take both alpha/mask into account."""
    app = FastAPI()
    cog = TilerFactory()
    app.include_router(cog.router)

    with TestClient(app) as client:
        cmap = urlencode(
            {
                "colormap": json.dumps(
                    [
                        # ([min, max], [r, g, b, a])
                        ([0, 1], [255, 255, 255, 0]),  # should be masked
                        ([2, 6000], [255, 0, 0, 255]),
                        ([6001, 300000], [0, 255, 0, 255]),
                    ]
                )
            }
        )

        response = client.get(f"/preview?url={DATA_DIR}/cog.tif&bidx=1&{cmap}")
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"

        with MemoryFile(response.content) as mem:
            with mem.open() as dst:
                img = dst.read()
                assert img[:, 0, 0].tolist() == [
                    0,
                    0,
                    0,
                    0,
                ]  # when creating a PNG, GDAL will set masked value to 0
                assert img[:, 500, 500].tolist() == [255, 0, 0, 255]