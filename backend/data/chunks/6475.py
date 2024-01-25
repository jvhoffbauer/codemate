    def __init__(
        self,
        id,
        country,
        province,
        coordinates,
        last_updated,
        confirmed,
        deaths,
        recovered,
    ):  # pylint: disable=too-many-arguments
        # General info.
        self.id = id
        self.country = country.strip()
        self.province = province.strip()
        self.coordinates = coordinates

        # Last update.
        self.last_updated = last_updated

        # Statistics.
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered