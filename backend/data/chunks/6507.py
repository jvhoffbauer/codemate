@cached(cache=TTLCache(maxsize=4, ttl=1800))
async def get_category(category):
    """
    Retrieves the data for the provided category. The data is cached for 30 minutes locally, 1 hour via shared Redis.

    :returns: The data for category.
    :rtype: dict
    """

    # Adhere to category naming standard.
    category = category.lower()
    data_id = f"jhu.{category}"

    # check shared cache
    cache_results = await check_cache(data_id)
    if cache_results:
        LOGGER.info(f"{data_id} using shared cache results")
        results = cache_results
    else:
        LOGGER.info(f"{data_id} shared cache empty")
        # URL to request data from.
        url = BASE_URL + "time_series_covid19_%s_global.csv" % category

        # Request the data
        LOGGER.info(f"{data_id} Requesting data...")
        async with httputils.CLIENT_SESSION.get(url) as response:
            text = await response.text()

        LOGGER.debug(f"{data_id} Data received")

        # Parse the CSV.
        data = list(csv.DictReader(text.splitlines()))
        LOGGER.debug(f"{data_id} CSV parsed")

        # The normalized locations.
        locations = []

        for item in data:
            # Filter out all the dates.
            dates = dict(
                filter(lambda element: date_util.is_date(element[0]), item.items())
            )

            # Make location history from dates.
            history = {date: int(float(amount or 0)) for date, amount in dates.items()}

            # Latest data insert value.
            latest = list(history.values())[-1]

            # Country for this location.
            country = item["Country/Region"]

            # Normalize the item and append to locations.
            locations.append(
                {
                    "country": country,
                    "country_code": countries.country_code(country),
                    "province": item["Province/State"],
                    "coordinates": {
                        "lat": item["Lat"],
                        "long": item["Long"],
                    },
                    "history": history,
                    "latest": int(latest or 0),
                }
            )
        LOGGER.debug(f"{data_id} Data normalized")

        # Latest total.
        latest = sum(map(lambda location: location["latest"], locations))

        # Return the final data.
        results = {
            "locations": locations,
            "latest": latest,
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "source": "https://github.com/ExpDev07/coronavirus-tracker-api",
        }
        # save the results to distributed cache
        await load_cache(data_id, results)

    LOGGER.info(f"{data_id} results:\n{pf(results, depth=1)}")
    return results