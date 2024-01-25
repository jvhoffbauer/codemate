@cached(cache=TTLCache(maxsize=1, ttl=1800))
async def get_locations():
    """
    Retrieves the locations from the categories. The locations are cached for 1 hour.

    :returns: The locations.
    :rtype: List[Location]
    """

    data_id = "jhu.locations"
    LOGGER.info(f"pid:{PID}: {data_id} Requesting data...")

    # Get all of the data categories locations.
    confirmed = await get_category("confirmed")
    deaths = await get_category("deaths")
    recovered = await get_category("recovered")

    locations_confirmed = confirmed["locations"]
    locations_deaths = deaths["locations"]
    locations_recovered = recovered["locations"]

    # Final locations to return.
    locations = []
    # ***************************************************************************
    # TODO: This iteration approach assumes the indexes remain the same
    #       and opens us to a CRITICAL ERROR. The removal of a column in the data source
    #       would break the API or SHIFT all the data confirmed, deaths, recovery producting
    #       incorrect data to consumers.
    # ***************************************************************************
    # Go through locations.
    for index, location in enumerate(locations_confirmed):
        # Get the timelines.

        # TEMP: Fix for merging recovery data. See TODO above for more details.
        key = (location["country"], location["province"])

        timelines = {
            "confirmed": location["history"],
            "deaths": parse_history(key, locations_deaths),
            "recovered": parse_history(key, locations_recovered),
        }

        # Grab coordinates.
        coordinates = location["coordinates"]

        # Create location (supporting timelines) and append.
        locations.append(
            TimelinedLocation(
                id=index,
                country=location["country"],
                province=location["province"],
                coordinates=Coordinates(
                    latitude=coordinates["lat"], longitude=coordinates["long"]
                ),
                last_updated=datetime.utcnow().isoformat() + "Z",
                timelines={
                    "confirmed": Timeline(
                        timeline={
                            datetime.strptime(date, "%m/%d/%y").isoformat()
                            + "Z": amount
                            for date, amount in timelines["confirmed"].items()
                        }
                    ),
                    "deaths": Timeline(
                        timeline={
                            datetime.strptime(date, "%m/%d/%y").isoformat()
                            + "Z": amount
                            for date, amount in timelines["deaths"].items()
                        }
                    ),
                    "recovered": Timeline(
                        timeline={
                            datetime.strptime(date, "%m/%d/%y").isoformat()
                            + "Z": amount
                            for date, amount in timelines["recovered"].items()
                        }
                    ),
                },
            )
        )

    LOGGER.info(f"{data_id} Data normalized")

    return locations