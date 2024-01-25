@needs_py39
@pytest.mark.parametrize(
    "path,cookies,expected_status,expected_response",
    [
        ("/items", None, 200, {"ads_id": None}),
        ("/items", {"ads_id": "ads_track"}, 200, {"ads_id": "ads_track"}),
        (
            "/items",
            {"ads_id": "ads_track", "session": "cookiesession"},
            200,
            {"ads_id": "ads_track"},
        ),
        ("/items", {"session": "cookiesession"}, 200, {"ads_id": None}),
    ],
)
def test(path, cookies, expected_status, expected_response):
    from docs_src.cookie_params.tutorial001_an_py39 import app

    client = TestClient(app, cookies=cookies)
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response