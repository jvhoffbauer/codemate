    def __post_init__(self):
        """Post Init."""
        if not self.bands and not self.expression:
            raise MissingBands(
                "bands must be defined either via expression or bands options."
            )