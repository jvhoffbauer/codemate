def test_class_dependency(route, value):
    response = client.get(route, params={"value": value})
    assert response.status_code == 200, response.text
    assert response.json() == value