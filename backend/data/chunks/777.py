def test_filter_truncates_correlation_id(cid: str, log_record: LogRecord):
    filter_ = CorrelationIdFilter(uuid_length=8)

    assert not hasattr(log_record, "correlation_id")
    filter_.filter(log_record)
    assert len(log_record.correlation_id) == 8  # Needs to match uuid_length
    assert cid.startswith(
        log_record.correlation_id
    )  # And needs to be the first 8 characters of the id