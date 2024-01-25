def test_is_uploadfile_sequence_annotation():
    # For coverage
    # TODO: in theory this would allow declaring types that could be lists of UploadFile
    # and other types, but I'm not even sure it's a good idea to support it as a first
    # class "feature"
    assert is_uploadfile_sequence_annotation(Union[List[str], List[UploadFile]])