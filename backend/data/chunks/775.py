def test_filter_has_default_value_attributes():
    filter_ = CorrelationIdFilter(default_value="-")
    assert filter_.default_value == "-"