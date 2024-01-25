async def get_locations():
    """
    Returns a list containing parsed NYT data by US county. The data is cached for 1 hour.

    :returns: The complete data for US Counties.
    :rtype: dict
    """
    data_id = "nyt.locations"
    # Request the data.
    LOGGER.info(f"{data_id} Requesting data...")
    # check shared cache
    cache_results = await check_cache(data_id)
    if cache_results:
        LOGGER.info(f"{data_id} using shared cache results")
        locations = cache_results
    else:
        LOGGER.info(f"{data_id} shared cache empty")
        async with httputils.CLIENT_SESSION.get(BASE_URL) as response:
            text = await response.text()

        LOGGER.debug(f"{data_id} Data received")

        # Parse the CSV.
        data = list(csv.DictReader(text.splitlines()))
        LOGGER.debug(f"{data_id} CSV parsed")

        # Group together locations (NYT data ordered by dates not location).
        grouped_locations = get_grouped_locations_dict(data)

        # The normalized locations.
        locations = []

        for idx, (county_state, histories) in enumerate(grouped_locations.items()):
            # Make location history for confirmed and deaths from dates.
            # List is tuples of (date, amount) in order of increasing dates.
            confirmed_list = histories["confirmed"]
            confirmed_history = {
                date: int(amount or 0) for date, amount in confirmed_list
            }

            deaths_list = histories["deaths"]
            deaths_history = {date: int(amount or 0) for date, amount in deaths_list}

            # Normalize the item and append to locations.
            locations.append(
                NYTLocation(
                    id=idx,
                    state=county_state[1],
                    county=county_state[0],
                    coordinates=Coordinates(
                        None, None
                    ),  # NYT does not provide coordinates
                    last_updated=datetime.utcnow().isoformat()
                    + "Z",  # since last request
                    timelines={
                        "confirmed": Timeline(
                            timeline={
                                datetime.strptime(date, "%Y-%m-%d").isoformat()
                                + "Z": amount
                                for date, amount in confirmed_history.items()
                            }
                        ),
                        "deaths": Timeline(
                            timeline={
                                datetime.strptime(date, "%Y-%m-%d").isoformat()
                                + "Z": amount
                                for date, amount in deaths_history.items()
                            }
                        ),
                        "recovered": Timeline(),
                    },
                )
            )
        LOGGER.info(f"{data_id} Data normalized")
        # save the results to distributed cache
        # TODO: fix json serialization
        try:
            await load_cache(data_id, locations)
        except TypeError as type_err:
            LOGGER.error(type_err)

    return locations