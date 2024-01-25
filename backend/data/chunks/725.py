    def cleanup(**kwargs: Any) -> None:
        """
        Clear context vars, to avoid re-using values in the next task.

        Context vars are cleared automatically in a HTTP request-setting,
        but must be manually reset for workers.
        """
        correlation_id.set(None)