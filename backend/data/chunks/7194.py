    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)