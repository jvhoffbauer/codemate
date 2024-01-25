def test_celery_filter_has_uuid_length_attributes():
    filter_ = CeleryTracingIdsFilter(uuid_length=8)
    assert filter_.uuid_length == 8