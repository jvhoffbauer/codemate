@dataclass
class AssetsBidxParams(AssetsParams):
    """Assets, Asset's band Indexes and Asset's band Expression parameters."""

    asset_indexes: Optional[Sequence[str]] = Query(
        None,
        title="Per asset band indexes",
        description="Per asset band indexes",
        alias="asset_bidx",
        examples={
            "one-asset": {
                "description": "Return indexes 1,2,3 of asset `data`.",
                "value": ["data|1;2;3"],
            },
            "multi-assets": {
                "description": "Return indexes 1,2,3 of asset `data` and indexes 1 of asset `cog`",
                "value": ["data|1;2;3", "cog|1"],
            },
        },
    )

    asset_expression: Optional[Sequence[str]] = Query(
        None,
        title="Per asset band expression",
        description="Per asset band expression",
        examples={
            "one-asset": {
                "description": "Return results for expression `b1*b2+b3` of asset `data`.",
                "value": ["data|b1*b2+b3"],
            },
            "multi-assets": {
                "description": "Return results for expressions `b1*b2+b3` for asset `data` and `b1+b3` for asset `cog`.",
                "value": ["data|b1*b2+b3", "cog|b1+b3"],
            },
        },
    )

    def __post_init__(self):
        """Post Init."""
        if self.asset_indexes:
            self.asset_indexes: Dict[str, Sequence[int]] = {  # type: ignore
                idx.split("|")[0]: list(map(int, idx.split("|")[1].split(",")))
                for idx in self.asset_indexes
            }

        if self.asset_expression:
            self.asset_expression: Dict[str, str] = {  # type: ignore
                idx.split("|")[0]: idx.split("|")[1] for idx in self.asset_expression
            }