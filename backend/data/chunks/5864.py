    def create_item(self, item: Dict[str, Any]) -> TableModelT:
        """Create a database orm object through a dictionary."""
        return self.model(**item)