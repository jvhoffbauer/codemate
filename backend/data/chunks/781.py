def test_celery_filter_adds_parent_id(cid: str, log_record: LogRecord):
    filter_ = CeleryTracingIdsFilter()
    celery_parent_id.set("a")

    assert not hasattr(log_record, "celery_parent_id")
    filter_.filter(log_record)
    assert log_record.celery_parent_id == "a"