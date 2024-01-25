def test_celery_filter_adds_current_id(cid: str, log_record: LogRecord):
    filter_ = CeleryTracingIdsFilter()
    celery_current_id.set("b")

    assert not hasattr(log_record, "celery_current_id")
    filter_.filter(log_record)
    assert log_record.celery_current_id == "b"