async def teardown_client_session():
    """Close the application-global aiohttp.ClientSession."""
    global CLIENT_SESSION  # pylint: disable=global-statement
    LOGGER.info("Closing global aiohttp.ClientSession.")
    await CLIENT_SESSION.close()