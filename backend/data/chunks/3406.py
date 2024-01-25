def test_dependency_set_status_code():
    response = client.delete("/1")
    assert response.status_code == 400 and response.content
    assert response.json() == {"msg": "Status overwritten", "id": 1}