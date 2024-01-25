def get_settings(**kwargs) -> BaseSettings:
    """
    Read settings from the environment or `.env` file.
    https://pydantic-docs.helpmanual.io/usage/settings/#dotenv-env-support

    Usage:
        import app.config

        settings = app.config.get_settings(_env_file="")
        port_number = settings.port
    """
    CFG_LOGGER.info("Loading Config settings from Environment ...")
    return _Settings(**kwargs)