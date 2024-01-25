def test_get_path(health_client, path, expected_status, expected_response):
    resp = health_client.get(path)
    assert resp.status_code == expected_status
    if resp.status_code == 200:
        assert resp.json() == expected_response