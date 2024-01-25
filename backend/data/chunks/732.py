    def clean_up(**kwargs: Any) -> None:
        """
        Clear context vars, to avoid re-using values in the next task.
        """
        celery_current_id.set(None)
        celery_parent_id.set(None)