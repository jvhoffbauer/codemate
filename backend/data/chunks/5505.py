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