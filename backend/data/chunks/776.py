def test_filter_adds_correlation_id(cid: str, log_record: LogRecord):
    filter_ = CorrelationIdFilter()

    assert not hasattr(log_record, "correlation_id")
    filter_.filter(log_record)
    assert log_record.correlation_id == cid