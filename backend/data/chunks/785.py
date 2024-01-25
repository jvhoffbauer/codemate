def test_celery_filter_truncates_current_id_correctly(
    cid: str, log_record: LogRecord, uuid_length, expected
):
    """
    If uuid is unspecified, the default should be 36.

    Otherwise, the id should be truncated to the specified length.
    """
    filter_ = CeleryTracingIdsFilter(uuid_length=uuid_length)
    celery_id = str(uuid4())
    celery_current_id.set(celery_id)

    assert not hasattr(log_record, "celery_current_id")
    filter_.filter(log_record)
    assert log_record.celery_current_id == celery_id[:expected]