def test_paths_level5(override1, override2, override3, override4, override5):
    url = ""
    content_type_level = "0"
    if override1:
        url += "/level1"
        content_type_level = "1"
    if override2:
        url += "/level2"
        content_type_level = "2"
    if override3:
        url += "/level3"
        content_type_level = "3"
    if override4:
        url += "/level4"
        content_type_level = "4"
    if override5:
        url += "/override5"
        content_type_level = "5"
    else:
        url += "/default5"
    url += "?level5=foo"
    response = client.get(url)
    assert response.json() == "foo"
    assert (
        response.headers["content-type"] == f"application/x-level-{content_type_level}"
    )
    assert "x-level0" in response.headers
    assert not override1 or "x-level1" in response.headers
    assert not override2 or "x-level2" in response.headers
    assert not override3 or "x-level3" in response.headers
    assert not override4 or "x-level4" in response.headers
    assert not override5 or "x-level5" in response.headers