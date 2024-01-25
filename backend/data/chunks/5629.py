def test_imageprofile(driver):
    """test image profile."""
    assert ImageType[driver].profile == img_profiles.get(driver)