def test_info(httpx, rio, app):
    """test /info endpoint."""
    httpx.get = mock_RequestGet
    rio.open = mock_rasterio_open

    response = app.get("/stac/assets?url=https://myurl.com/item.json")
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 2

    response = app.get("/stac/info?url=https://myurl.com/item.json&assets=B01")
    assert response.status_code == 200
    body = response.json()
    assert body["B01"]

    response = app.get("/stac/info?url=https://myurl.com/item.json")
    assert response.status_code == 200
    body = response.json()
    assert body["B01"]
    assert body["B09"]

    response = app.get(
        "/stac/info?url=https://myurl.com/item.json&assets=B01&assets=B09"
    )
    assert response.status_code == 200
    body = response.json()
    assert body["B01"]
    assert body["B09"]

    response = app.get("/stac/info.geojson?url=https://myurl.com/item.json&assets=B01")
    assert response.status_code == 200
    body = response.json()
    assert response.headers["content-type"] == "application/geo+json"
    body = response.json()
    assert body["geometry"]
    assert body["properties"]["B01"]