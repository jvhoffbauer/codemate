def country_code(value):
    """
    Return two letter country code (Alpha-2) according to https://en.wikipedia.org/wiki/ISO_3166-1
    Defaults to "XX".
    """
    code = COUNTRY_NAME__COUNTRY_CODE.get(value, DEFAULT_COUNTRY_CODE)
    if code == DEFAULT_COUNTRY_CODE:
        # log at sub DEBUG level
        LOGGER.log(5, f"No country code found for '{value}'. Using '{code}'!")

    return code