def test_get_enums_lenet():
    response = client.get("/models/lenet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "lenet", "message": "LeCNN all the images"}