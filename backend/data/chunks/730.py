    def worker_prerun(task_id: str, task: "Task", **kwargs: Any) -> None:
        """
        Set current ID, and parent ID if it exists.
        """
        parent_id = task.request.get(header_key)
        if parent_id:
            celery_parent_id.set(parent_id)

        celery_id = task_id if use_internal_celery_task_id else generator()
        celery_current_id.set(celery_id)