def test_auth_using_prediction_api_no_apikey_header(test_client) -> None:
    response = test_client.post("/api/model/predict")
    assert response.status_code == 400
    assert response.json() == {"detail": messages.NO_API_KEY}