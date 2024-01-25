def _configure_logging():
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "correlation_id": {"()": "asgi_correlation_id.CorrelationIdFilter"},
            "celery_tracing": {"()": "asgi_correlation_id.CeleryTracingIdsFilter"},
        },
        "formatters": {
            "full": {
                "class": "logging.Formatter",
                "datefmt": "%H:%M:%S",
                "format": "[%(correlation_id)s] [%(celery_parent_id)s-%(celery_current_id)s] %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "filters": ["correlation_id", "celery_tracing"],
                "formatter": "full",
            },
        },
        "loggers": {
            # project logger
            "asgi_correlation_id": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }
    dictConfig(LOGGING)