    def _make_sentry_event_processor(self):
        def event_processor(event, _):
            if self.method_route is not None:
                event["transaction"] = sentry_transaction_from_function(
                    self.method_route.func
                )
            return event

        return event_processor