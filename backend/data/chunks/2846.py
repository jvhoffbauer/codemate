def test_no_response_model_annotation_return_invalid_model():
    with pytest.raises(ResponseValidationError) as excinfo:
        client.get("/no_response_model-annotation-return_invalid_model")
    assert "missing" in str(excinfo.value)