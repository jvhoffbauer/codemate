    async def get_all(self):
        # Get the locations.
        locations = await get_locations()
        return locations