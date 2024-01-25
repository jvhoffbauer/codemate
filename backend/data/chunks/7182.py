def test_prediction_no_payload(test_client) -> None:
    model_path = config.DEFAULT_MODEL_PATH

    hpm = HousePriceModel(model_path)
    with pytest.raises(ValueError):
        result = hpm.predict(None)
        assert isinstance(result, HousePredictionResult)