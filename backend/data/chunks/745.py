async def test_endpoint_to_worker_to_worker(
    client, caplog, celery_session_app, celery_session_worker
):
    """
    We expect:
        - The correlation ID to persist from the endpoint to the final worker
        - The current ID of the first worker to be added as the parent ID of the second worker
    """

    @default_app.get("/celery-test", status_code=200)
    async def test_view():
        logger.debug("Test view")
        task1.delay().get(timeout=10)

    caplog.set_level("DEBUG")

    cid = uuid4().hex
    await client.get("celery-test", headers={"X-Request-ID": cid})

    # Check the view record
    assert caplog.records[0].correlation_id == cid
    assert caplog.records[0].celery_current_id is None
    assert caplog.records[0].celery_parent_id is None

    last_current_id = None

    for record in caplog.records[1:3]:
        # Check that the correlation ID is persisted
        assert record.correlation_id == cid

        # Make sure the celery current ID is a valid UUID and present
        assert UUID(record.celery_current_id)

        # Make sure the parent ID matches the previous current ID
        assert record.celery_parent_id == last_current_id

        last_current_id = record.celery_current_id