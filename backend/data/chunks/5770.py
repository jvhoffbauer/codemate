@patch("rio_tiler.io.rasterio.rasterio")
def test_json_response_with_nan(rio, app):
    """test /info endpoint."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/info?url=https://myurl.com/cog_with_nan.tif")
    assert response.status_code == 200
    body = response.json()
    assert body["dtype"] == "float32"
    assert body["nodata_type"] == "Nodata"
    assert body["nodata_value"] is None

    response = app.get("/cog/info.geojson?url=https://myurl.com/cog_with_nan.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    body = response.json()
    assert body["geometry"]
    assert body["properties"]["nodata_type"] == "Nodata"
    assert body["properties"]["nodata_value"] is None

    response = app.get(
        "/cog/point/79.80860440702253,21.852217086223234?url=https://myurl.com/cog_with_nan.tif"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["values"][0] is None