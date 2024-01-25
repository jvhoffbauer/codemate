def test(path, cookies, expected_status, expected_response):
    from docs_src.cookie_params.tutorial001_py310 import app

    client = TestClient(app, cookies=cookies)
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response