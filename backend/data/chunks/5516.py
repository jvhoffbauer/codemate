@dataclass
class StatisticsParams(DefaultDependency):
    """Statistics options."""

    categorical: bool = Query(
        False, description="Return statistics for categorical dataset."
    )
    categories: List[Union[float, int]] = Query(
        None,
        alias="c",
        title="Pixels values for categories.",
        description="List of values for which to report counts.",
        example=[1, 2, 3],
    )
    percentiles: List[int] = Query(
        [2, 98],
        alias="p",
        title="Percentile values",
        description="List of percentile values.",
        example=[2, 5, 95, 98],
    )