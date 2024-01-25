def fetch_populations(save=False):
    """
    Returns a dictionary containing the population of each country fetched from the GeoNames.
    https://www.geonames.org/

    TODO: only skip writing to the filesystem when deployed with gunicorn, or handle concurent access, or use DB.

    :returns: The mapping of populations.
    :rtype: dict
    """
    LOGGER.info("Fetching populations...")

    # Mapping of populations
    mappings = {}

    # Fetch the countries.
    try:
        countries = requests.get(
            GEONAMES_URL, params={"username": "dperic"}, timeout=1.25
        ).json()["geonames"]
        # Go through all the countries and perform the mapping.
        for country in countries:
            mappings.update(
                {country["countryCode"]: int(country["population"]) or None}
            )

        if mappings and save:
            LOGGER.info(
                f"Saving population data to {app.io.save(GEONAMES_BACKUP_PATH, mappings)}"
            )
    except (json.JSONDecodeError, KeyError, requests.exceptions.Timeout) as err:
        LOGGER.warning(
            f"Error pulling population data. {err.__class__.__name__}: {err}"
        )
        mappings = app.io.load(GEONAMES_BACKUP_PATH)
        LOGGER.info(f"Using backup data from {GEONAMES_BACKUP_PATH}")
    # Finally, return the mappings.
    LOGGER.info("Fetched populations")
    return mappings