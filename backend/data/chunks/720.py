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