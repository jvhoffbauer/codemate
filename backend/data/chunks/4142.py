def test_get_enums_resnet():
    response = client.get("/models/resnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "resnet", "message": "Have some residuals"}