def test_duplicates():
    response = client.post("/with-duplicates", json={"data": "myitem"})
    assert response.status_code == 200, response.text
    assert response.json() == [{"data": "myitem"}, {"data": "myitem"}]