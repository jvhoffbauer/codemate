def setup_sentry(app):
    import sentry_sdk

    sentry_sdk.init(
        "sentry_sdk",
    )