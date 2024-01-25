def set_transaction_id(correlation_id: str) -> None:
    """
    Set Sentry's event transaction ID as the current correlation ID.

    The transaction ID is displayed in a Sentry event's detail view,
    which makes it easier to correlate logs to specific events.
    """
    from sentry_sdk import configure_scope

    with configure_scope() as scope:
        scope.set_tag("transaction_id", correlation_id)