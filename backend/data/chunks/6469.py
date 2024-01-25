    def serialize(self):
        """
        Serialize the model into dict
        TODO: override dict() instead of using serialize
        """
        return {**self.dict(), "latest": self.latest}