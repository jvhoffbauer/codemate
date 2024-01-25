@dataclass
class AssetsBidxExprParams(DefaultDependency):
    """Assets, Expression and Asset's band Indexes parameters."""

    assets: Optional[List[str]] = Query(
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
    expression: Optional[str] = Query(
        None,
        title="Band Math expression",
        description="Band math expression between assets",
        examples={
            "simple": {
                "description": "Return results of expression between assets.",
                "value": "asset1_b1 + asset2_b1 / asset3_b1",
            },
        },
    )

    asset_indexes: Optional[Sequence[str]] = Query(
        None,
        title="Per asset band indexes",
        description="Per asset band indexes (coma separated indexes)",
        alias="asset_bidx",
        examples={
            "one-asset": {
                "description": "Return indexes 1,2,3 of asset `data`.",
                "value": ["data|1,2,3"],
            },
            "multi-assets": {
                "description": "Return indexes 1,2,3 of asset `data` and indexes 1 of asset `cog`",
                "value": ["data|1,2,3", "cog|1"],
            },
        },
    )

    asset_as_band: Optional[bool] = Query(
        None,
        title="Consider asset as a 1 band dataset",
        description="Asset as Band",
    )

    def __post_init__(self):
        """Post Init."""
        if not self.assets and not self.expression:
            raise MissingAssets(
                "assets must be defined either via expression or assets options."
            )

        if self.asset_indexes:
            self.asset_indexes: Dict[str, Sequence[int]] = {  # type: ignore
                idx.split("|")[0]: list(map(int, idx.split("|")[1].split(",")))
                for idx in self.asset_indexes
            }