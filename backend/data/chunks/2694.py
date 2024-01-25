def test_value_extracting_by_http():
    response = client.get("/http")
    assert response.status_code == 200
    assert response.json() == 42