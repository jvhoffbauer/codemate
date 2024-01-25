    def filter(self, record: "LogRecord") -> bool:
        """
        Append a parent- and current ID to the log record.

        The celery current ID is a unique ID generated for each new worker process.
        The celery parent ID is the current ID of the worker process that spawned
        the current process. If the worker process was spawned by a beat process
        or from an endpoint, the parent ID will be None.
        """
        pid = celery_parent_id.get(self.default_value)
        record.celery_parent_id = _trim_string(pid, self.uuid_length)
        cid = celery_current_id.get(self.default_value)
        record.celery_current_id = _trim_string(cid, self.uuid_length)
        return True