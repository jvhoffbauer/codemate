    @property
    def country_code(self):
        """
        Gets the alpha-2 code represention of the country. Returns 'XX' if none is found.

        :returns: The country code.
        :rtype: str
        """
        return (
            countries.country_code(self.country) or countries.DEFAULT_COUNTRY_CODE
        ).upper()