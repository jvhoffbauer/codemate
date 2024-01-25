def test_imagetype(value, driver, mediatype):
    """Test driver and mediatype values."""
    assert ImageType[value].driver == driver
    assert ImageType[value].mediatype == mediatype