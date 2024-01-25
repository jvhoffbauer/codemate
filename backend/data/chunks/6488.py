async def get_deaths():
    """Total deaths."""
    deaths_data = await get_category("deaths")

    return deaths_data