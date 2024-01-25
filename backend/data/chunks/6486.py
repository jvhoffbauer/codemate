async def get_confirmed():
    """Confirmed cases."""
    confirmed_data = await get_category("confirmed")

    return confirmed_data