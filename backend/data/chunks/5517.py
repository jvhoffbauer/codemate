@dataclass
class HistogramParams(DefaultDependency):
    """Numpy Histogram options."""

    bins: Optional[str] = Query(
        None,
        alias="histogram_bins",
        title="Histogram bins.",
        description="""
Defines the number of equal-width bins in the given range (10, by default).

If bins is a sequence (comma `,` delimited values), it defines a monotonically increasing array of bin edges, including the rightmost edge, allowing for non-uniform bin widths.

link: https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
        """,
        examples={
            "simple": {
                "description": "Defines the number of equal-width bins",
                "value": 8,
            },
            "array": {
                "description": "Defines custom bin edges (comma `,` delimited values)",
                "value": "0,100,200,300",
            },
        },
    )

    range: Optional[str] = Query(
        None,
        alias="histogram_range",
        title="Histogram range",
        description="""
Comma `,` delimited range of the bins.

The lower and upper range of the bins. If not provided, range is simply (a.min(), a.max()).

Values outside the range are ignored. The first element of the range must be less than or equal to the second.
range affects the automatic bin computation as well.

link: https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
        """,
        example="0,1000",
    )

    def __post_init__(self):
        """Post Init."""
        if self.bins:
            bins = self.bins.split(",")
            if len(bins) == 1:
                self.bins = int(bins[0])  # type: ignore
            else:
                self.bins = list(map(float, bins))  # type: ignore
        else:
            self.bins = 10

        if self.range:
            self.range = list(map(float, self.range.split(",")))  # type: ignore