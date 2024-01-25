def test_response_model_no_annotation_return_invalid_model():
    with pytest.raises(ResponseValidationError) as excinfo:
        client.get("/response_model-no_annotation-return_invalid_model")
    assert "missing" in str(excinfo.value)