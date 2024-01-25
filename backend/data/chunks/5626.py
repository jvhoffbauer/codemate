@pytest.mark.parametrize(
    "value,driver,mediatype",
    [
        ("png", "PNG", "image/png"),
        ("npy", "NPY", "application/x-binary"),
        ("tif", "GTiff", "image/tiff; application=geotiff"),
        ("jpg", "JPEG", "image/jpg"),
        ("jpeg", "JPEG", "image/jpeg"),
        ("jp2", "JP2OpenJPEG", "image/jp2"),
        ("webp", "WEBP", "image/webp"),
        ("pngraw", "PNG", "image/png"),
    ],
)
def test_imagetype(value, driver, mediatype):
    """Test driver and mediatype values."""
    assert ImageType[value].driver == driver
    assert ImageType[value].mediatype == mediatype