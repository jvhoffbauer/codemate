def test_upload_file_dummy_with_info_plain_validator_function():
    # For coverage
    assert UploadFile.__get_pydantic_core_schema__(str, lambda x: None) == {}