- Tests whether `CeleryTracingIdsFilter` adds parent ID to logs using Celery's tracing context
- Sets a value for `celery_parent_id` in the tracing context before applying the filter
- Verifies that the filtered log record contains the expected parent ID