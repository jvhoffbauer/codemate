def get_sentry_extension() -> Callable[[str], None]:
    """
    Return set_transaction_id, if the Sentry-sdk is installed.
    """
    try:
        import sentry_sdk  # noqa: F401, TC002

        from asgi_correlation_id.extensions.sentry import set_transaction_id

        return set_transaction_id
    except ImportError:  # pragma: no cover
        return lambda correlation_id: None