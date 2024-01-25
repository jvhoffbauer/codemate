def test_celery_filter_maintains_current_behavior(cid: str, log_record: LogRecord):
    """Maintain default behavior with signature change

    Since the default values of CeleryTracingIdsFilter are being changed,
    the new default values should also not trim a hex uuid.
    """
    celery_id = uuid4().hex
    celery_current_id.set(celery_id)
    new_filter = CeleryTracingIdsFilter()

    assert not hasattr(log_record, "celery_current_id")
    new_filter.filter(log_record)
    assert log_record.celery_current_id == celery_id
    new_filter_record_id = log_record.celery_current_id

    del log_record.celery_current_id

    original_filter = CeleryTracingIdsFilter(uuid_length=32)
    assert not hasattr(log_record, "celery_current_id")
    original_filter.filter(log_record)
    assert log_record.celery_current_id == celery_id
    original_filter_record_id = log_record.celery_current_id

    assert original_filter_record_id == new_filter_record_id