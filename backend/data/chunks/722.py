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