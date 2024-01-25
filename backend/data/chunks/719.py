def load_correlation_ids(
    header_key: str = "CORRELATION_ID",
    generator: Callable[[], str] = uuid_hex_generator,
) -> None:
    """
    Transfer correlation IDs from a HTTP request to a Celery worker,
    when spawned from a request.

    This is called as long as Celery is installed.
    """
    from asgi_correlation_id.context import correlation_id

    sentry_extension = get_sentry_extension()

    @before_task_publish.connect(weak=False)
    def transfer_correlation_id(headers: Dict[str, str], **kwargs: Any) -> None:
        """
        Transfer correlation ID from request thread to Celery worker, by adding
        it as a header.

        This way we're able to correlate work executed by Celery workers, back
        to the originating request, when there was one.
        """
        cid = correlation_id.get()
        if cid:
            headers[header_key] = cid

    @task_prerun.connect(weak=False)
    def load_correlation_id(task: "Task", **kwargs: Any) -> None:
        """
        Set correlation ID from header if it exists.

        If it doesn't exist, generate a unique ID for the task anyway.
        """
        id_value = task.request.get(header_key)
        if id_value:
            correlation_id.set(id_value)
            sentry_extension(id_value)
        else:
            generated_correlation_id = generator()
            correlation_id.set(generated_correlation_id)
            sentry_extension(generated_correlation_id)

    @task_postrun.connect(weak=False)
    def cleanup(**kwargs: Any) -> None:
        """
        Clear context vars, to avoid re-using values in the next task.

        Context vars are cleared automatically in a HTTP request-setting,
        but must be manually reset for workers.
        """
        correlation_id.set(None)