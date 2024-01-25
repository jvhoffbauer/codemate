@dataclass
class BidxParams(DefaultDependency):
    """Band Indexes parameters."""

    indexes: Optional[List[int]] = Query(
        None,
        title="Band indexes",
        alias="bidx",
        description="Dataset band indexes",
        examples={"one-band": {"value": [1]}, "multi-bands": {"value": [1, 2, 3]}},
    )