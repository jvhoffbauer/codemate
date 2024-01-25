@dataclass
class AssetsParams(DefaultDependency):
    """Assets parameters."""

    assets: List[str] = Query(
        None,
        title="Asset names",
        description="Asset's names.",
        examples={
            "one-asset": {
                "description": "Return results for asset `data`.",
                "value": ["data"],
            },
            "multi-assets": {
                "description": "Return results for assets `data` and `cog`.",
                "value": ["data", "cog"],
            },
        },
    )