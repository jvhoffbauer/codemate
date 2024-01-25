async def get_latest(
    request: Request, source: Sources = Sources.JHU
):  # pylint: disable=unused-argument
    """
    Getting latest amount of total confirmed cases, deaths, and recoveries.
    """
    locations = await request.state.source.get_all()
    return {
        "latest": {
            "confirmed": sum(map(lambda location: location.confirmed, locations)),
            "deaths": sum(map(lambda location: location.deaths, locations)),
            "recovered": sum(map(lambda location: location.recovered, locations)),
        }
    }