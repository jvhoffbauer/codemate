@pytest.mark.parametrize(
    "driver",
    ["png", "pngraw", "jpg", "jpeg", "webp"],
)
def test_imageprofile(driver):
    """test image profile."""
    assert ImageType[driver].profile == img_profiles.get(driver)