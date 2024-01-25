async def get_recovered():
    """Recovered cases."""
    recovered_data = await get_category("recovered")

    return recovered_data