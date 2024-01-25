    def filter(self, record: "LogRecord") -> bool:
        """
        Attach a correlation ID to the log record.

        Since the correlation ID is defined in the middleware layer, any
        log generated from a request after this point can easily be searched
        for, if the correlation ID is added to the message, or included as
        metadata.
        """
        cid = correlation_id.get(self.default_value)
        record.correlation_id = _trim_string(cid, self.uuid_length)
        return True