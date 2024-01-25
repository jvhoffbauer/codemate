@patch("rio_tiler.io.rasterio.rasterio")
@patch("rio_tiler.io.stac.httpx")
def test_point(httpx, rio, app):
    """test crop endpoints."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    # Missing Assets or Expression
    response = app.get("/stac/point/23.878,32.063?url=https://myurl.com/item.json")
    assert response.status_code == 400

    response = app.get(
        "/stac/point/23.878,32.063?url=https://myurl.com/item.json&assets=B01"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["coordinates"] == [23.878, 32.063]
    assert body["values"] == [3565]
    assert body["band_names"] == ["B01_b1"]

    response = app.get(
        "/stac/point/23.878,32.063?url=https://myurl.com/item.json&expression=B01_b1*2"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["coordinates"] == [23.878, 32.063]
    assert body["values"] == [7130]
    assert body["band_names"] == ["B01_b1*2"]

    response = app.get(
        "/stac/point/23.878,32.063?url=https://myurl.com/item.json&expression=B01_b1/B09_b1"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["coordinates"] == [23.878, 32.063]
    assert round(body["values"][0], 2) == 0.49