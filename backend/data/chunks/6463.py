    def serialize(self):
        """
        Serializes the coordinates into a dict.

        :returns: The serialized coordinates.
        :rtype: dict
        """
        return {"latitude": self.latitude, "longitude": self.longitude}