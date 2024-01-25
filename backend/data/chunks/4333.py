def test_sub():
    response = client.get("/subapi/sub")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World from sub API"}