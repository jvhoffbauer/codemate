@dataclass
class BandsParams(DefaultDependency):
    """Band names parameters."""

    bands: List[str] = Query(
        None,
        title="Band names",
        description="Band's names.",
        examples={
            "one-band": {
                "description": "Return results for band `B01`.",
                "value": ["B01"],
            },
            "multi-bands": {
                "description": "Return results for bands `B01` and `B02`.",
                "value": ["B01", "B02"],
            },
        },
    )