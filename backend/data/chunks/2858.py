def test_response_model_model1_annotation_model2_return_invalid_model():
    with pytest.raises(ResponseValidationError) as excinfo:
        client.get("/response_model_model1-annotation_model2-return_invalid_model")
    assert "missing" in str(excinfo.value)