    def _name_to_id(self, text: str):
        """Utility function to do a messy normalization of an entity name

        text (str): text to create "id" from
        """
        return "-".join([s.lower() for s in text.split()])