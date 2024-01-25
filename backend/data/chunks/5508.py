@dataclass
class BandsExprParams(ExpressionParams, BandsParams):
    """Band names and Expression parameters (Band or Expression required)."""

    def __post_init__(self):
        """Post Init."""
        if not self.bands and not self.expression:
            raise MissingBands(
                "bands must be defined either via expression or bands options."
            )