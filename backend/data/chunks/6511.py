def parse_history(key: tuple, locations: list):
    """
    Helper for validating and extracting history content from
    locations data based on key. Validates with the current country/province
    key to make sure no index/column issue.
    """

    for i, location in enumerate(locations):
        if (location["country"], location["province"]) == key:
            return location["history"]

    LOGGER.debug(f"iteration data merge error: {key}")

    return {}