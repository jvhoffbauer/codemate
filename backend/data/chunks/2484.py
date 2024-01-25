def test_paths_level3(override1, override2, override3):
    url = ""
    content_type_level = "0"
    if override1:
        url += "/level1"
        content_type_level = "1"
    if override2:
        url += "/level2"
        content_type_level = "2"
    if override3:
        url += "/override3"
        content_type_level = "3"
    else:
        url += "/default3"
    url += "?level3=foo"
    response = client.get(url)
    assert response.json() == "foo"
    assert (
        response.headers["content-type"] == f"application/x-level-{content_type_level}"
    )
    assert "x-level0" in response.headers
    assert not override1 or "x-level1" in response.headers
    assert not override2 or "x-level2" in response.headers
    assert not override3 or "x-level3" in response.headers