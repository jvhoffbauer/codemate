def test_mosaic_not_found_error(app):
    """
    This should probably return a 404 but currently returns a 424 because cogeo_mosaic incorrectly raises a MosaicError
    instead of MosaicNotFoundError.
    """
    response = app.get("/mosaicjson", params={"url": "mosaic.json"})
    assert response.status_code == 424