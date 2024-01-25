def test_tile(app):
    """Test GET /mosaicjson/tiles endpoint"""
    mosaicjson = read_json_fixture(MOSAICJSON_FILE)
    bounds = mosaicjson["bounds"]
    tile = mercantile.tile(*mosaicjson["center"])
    partial_tile = mercantile.tile(bounds[0], bounds[1], mosaicjson["minzoom"])

    with patch.object(FileBackend, "_read", mosaic_read_factory(MOSAICJSON_FILE)):
        # full tile
        response = app.get(
            f"/mosaicjson/tiles/{tile.z}/{tile.x}/{tile.y}",
            params={"url": MOSAICJSON_FILE},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"
        meta = parse_img(response.content)
        assert meta["width"] == meta["height"] == 256

        response = app.get(
            f"/mosaicjson/tiles/{tile.z}/{tile.x}/{tile.y}@2x",
            params={"url": MOSAICJSON_FILE},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"
        meta = parse_img(response.content)
        assert meta["width"] == meta["height"] == 512

        response = app.get(
            f"/mosaicjson/tiles/{tile.z}/{tile.x}/{tile.y}.tif",
            params={"url": MOSAICJSON_FILE},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/tiff; application=geotiff"
        meta = parse_img(response.content)
        assert meta["width"] == meta["height"] == 256
        assert meta["crs"] == 3857

        response = app.get(
            f"/mosaicjson/tiles/{tile.z}/{tile.x}/{tile.y}@2x.tif",
            params={"url": MOSAICJSON_FILE, "nodata": 0, "bidx": 1},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/tiff; application=geotiff"
        meta = parse_img(response.content)
        assert meta["dtype"] == "uint16"
        assert meta["count"] == 2
        assert meta["width"] == 512
        assert meta["height"] == 512

        response = app.get(
            f"/mosaicjson/tiles/{tile.z}/{tile.x}/{tile.y}@2x.jpg",
            params={
                "url": MOSAICJSON_FILE,
                "rescale": "0,1000",
                "colormap_name": "viridis",
                "bidx": 1,
            },
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/jpg"

        # partial tile
        response = app.get(
            f"/mosaicjson/tiles/{partial_tile.z}/{partial_tile.x}/{partial_tile.y}",
            params={"url": MOSAICJSON_FILE},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/png"

        response = app.get(
            f"/mosaicjson/tiles/{partial_tile.z}/{partial_tile.x}/{partial_tile.y}.tif",
            params={"url": MOSAICJSON_FILE, "resampling": "bilinear"},
        )
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/tiff; application=geotiff"