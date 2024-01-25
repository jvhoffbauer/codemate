def test_celery_filter_has_default_value_attributes():
    filter_ = CeleryTracingIdsFilter(default_value="-")
    assert filter_.default_value == "-"