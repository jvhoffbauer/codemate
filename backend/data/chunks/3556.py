def test_upload_file_invalid():
    with pytest.raises(ValueError):
        UploadFile.validate("not a Starlette UploadFile")