async def test_worker_to_worker_to_worker(
    caplog, celery_session_app, celery_session_worker
):
    """
    We expect:
        - A correlation ID to be generated in the first worker and persisted to the final worker
        - The current ID of the first worker to be added as the
            parent ID of the second worker, and the same for 2 and 3
    """
    caplog.set_level("DEBUG")

    # Trigger task
    task1.delay().get(timeout=10)

    # Save first correlation ID
    first_log = caplog.records[0]
    first_cid = first_log.correlation_id

    last_current_id = None

    for record in caplog.records:
        # Check that the correlation ID is persisted
        assert record.correlation_id == first_cid

        # Make sure the celery current ID is a valid UUID and present
        assert UUID(record.celery_current_id)

        # Make sure the parent ID matches the previous current ID
        assert record.celery_parent_id == last_current_id

        last_current_id = record.celery_current_id