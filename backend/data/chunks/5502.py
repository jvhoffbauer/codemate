@dataclass
class AssetsBidxExprParamsOptional(AssetsBidxExprParams):
    """Assets, Expression and Asset's band Indexes parameters but with no requirement."""

    def __post_init__(self):
        """Post Init."""
        if self.asset_indexes:
            self.asset_indexes: Dict[str, Sequence[int]] = {  # type: ignore
                idx.split("|")[0]: list(map(int, idx.split("|")[1].split(",")))
                for idx in self.asset_indexes
            }