    @before_task_publish.connect(weak=False)
    def publish_task_from_worker_or_request(
        headers: Dict[str, str], **kwargs: Any
    ) -> None:
        """
        Transfer the current ID to the next Celery worker, by adding
        it as a header.

        This way we're able to tell which process spawned the next task.
        """
        current = celery_current_id.get()
        if current:
            headers[header_key] = current