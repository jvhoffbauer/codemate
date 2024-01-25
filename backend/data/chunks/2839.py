def test_response_model_no_annotation_return_invalid_dict():
    with pytest.raises(ResponseValidationError) as excinfo:
        client.get("/response_model-no_annotation-return_invalid_dict")
    assert "missing" in str(excinfo.value)