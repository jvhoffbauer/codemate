async def setup_client_session():
    """Set up the application-global aiohttp.ClientSession instance.

    aiohttp recommends that only one ClientSession exist for the lifetime of an application.
    See: https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request

    """
    global CLIENT_SESSION  # pylint: disable=global-statement
    LOGGER.info("Setting up global aiohttp.ClientSession.")
    CLIENT_SESSION = ClientSession()