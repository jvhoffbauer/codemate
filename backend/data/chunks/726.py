def load_celery_current_and_parent_ids(
    header_key: str = "CELERY_PARENT_ID",
    generator: Callable[[], str] = uuid_hex_generator,
    use_internal_celery_task_id: bool = False,
) -> None:
    """
    Configure Celery event hooks for generating tracing IDs with depth.

    This is not called automatically by the middleware.
    To use this, users should manually run it during startup.
    """
    from asgi_correlation_id.context import celery_current_id, celery_parent_id

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

    @task_prerun.connect(weak=False)
    def worker_prerun(task_id: str, task: "Task", **kwargs: Any) -> None:
        """
        Set current ID, and parent ID if it exists.
        """
        parent_id = task.request.get(header_key)
        if parent_id:
            celery_parent_id.set(parent_id)

        celery_id = task_id if use_internal_celery_task_id else generator()
        celery_current_id.set(celery_id)

    @task_postrun.connect(weak=False)
    def clean_up(**kwargs: Any) -> None:
        """
        Clear context vars, to avoid re-using values in the next task.
        """
        celery_current_id.set(None)
        celery_parent_id.set(None)