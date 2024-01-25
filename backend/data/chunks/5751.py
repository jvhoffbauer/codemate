@patch("rio_tiler.io.rasterio.rasterio")
def test_info(rio, app):
    """test /info endpoint."""
    rio.open = mock_rasterio_open

    response = app.get("/cog/info?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    body = response.json()
    assert len(body["bounds"]) == 4
    assert body["band_descriptions"] == [["b1", ""]]
    assert body["dtype"] == "uint16"
    assert body["colorinterp"] == ["gray"]
    assert body["nodata_type"] == "None"

    response = app.get("/cog/info.geojson?url=https://myurl.com/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    body = response.json()
    assert body["geometry"]
    assert body["properties"]["band_descriptions"] == [["b1", ""]]
    assert body["properties"]["dtype"] == "uint16"
    assert body["properties"]["colorinterp"] == ["gray"]
    assert body["properties"]["nodata_type"] == "None"