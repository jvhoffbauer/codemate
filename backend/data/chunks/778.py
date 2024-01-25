def test_filter_uses_default_value(cid: str, log_record: LogRecord):
    """
    We expect the filter to set the log record attribute to the default value
    if the context variable is not set.
    """
    filter_ = CorrelationIdFilter(default_value="-")
    correlation_id.reset(correlation_id_token)

    assert not hasattr(log_record, "correlation_id")
    filter_.filter(log_record)
    assert log_record.correlation_id == "-"