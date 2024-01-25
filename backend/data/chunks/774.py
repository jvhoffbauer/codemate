def test_filter_has_uuid_length_attributes():
    filter_ = CorrelationIdFilter(uuid_length=8)
    assert filter_.uuid_length == 8