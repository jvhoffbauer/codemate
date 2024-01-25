def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("https://myurl.com/")
    asset = asset.replace("https://myurl.com", DATA_DIR)
    return rasterio.open(asset)