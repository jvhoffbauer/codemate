- Retrieves population data from GeoNames using an API request
- Saves the retrieved data to a file named `geonames.json` by default, but skips saving it if the `save` parameter is set to False
- Loads previously saved data instead of making another API call if there's an error during the initial request
- Returns a dictionary containing the population of each country