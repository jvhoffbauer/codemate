def test_mosaic_auth_error(app):
    """Raise auth error 401."""
    response = app.get("/mosaicjson", params={"url": "s3://bucket/mosaic.json"})
    assert response.status_code == 401