def test_events():
    assert not ml_models, "ml_models should be empty"
    with TestClient(app) as client:
        assert ml_models["answer_to_everything"] == fake_answer_to_everything_ml_model
        response = client.get("/predict", params={"x": 2})
        assert response.status_code == 200, response.text
        assert response.json() == {"result": 84.0}
    assert not ml_models, "ml_models should be empty"