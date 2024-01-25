def test_response():
    response = client.get("/", headers={"someheader": "hello"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"dep1": "hello", "dep2": "hello123"}