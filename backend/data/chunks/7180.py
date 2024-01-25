def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict", json={}, headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422