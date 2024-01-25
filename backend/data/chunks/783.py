def test_celery_filter_uses_default_value(cid: str, log_record: LogRecord):
    """
    We expect the filter to set the log record attributes to the default value
    if the context variables are not not set.
    """
    filter_ = CeleryTracingIdsFilter(default_value="-")
    celery_parent_id.reset(celery_parent_id_token)
    celery_current_id.reset(celery_current_id_token)

    assert not hasattr(log_record, "celery_parent_id")
    assert not hasattr(log_record, "celery_current_id")
    filter_.filter(log_record)
    assert log_record.celery_parent_id == "-"
    assert log_record.celery_current_id == "-"