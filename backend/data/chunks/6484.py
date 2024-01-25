async def all_categories():
    """Get all the categories."""
    confirmed = await get_category("confirmed")
    deaths = await get_category("deaths")
    recovered = await get_category("recovered")

    return {
        # Data.
        "confirmed": confirmed,
        "deaths": deaths,
        "recovered": recovered,
        # Latest.
        "latest": {
            "confirmed": confirmed["latest"],
            "deaths": deaths["latest"],
            "recovered": recovered["latest"],
        },
    }