        def event_processor(event, _):
            if self.method_route is not None:
                event["transaction"] = sentry_transaction_from_function(
                    self.method_route.func
                )
            return event