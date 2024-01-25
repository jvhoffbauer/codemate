@dataclass
class CustomRenderParams(ImageRenderingParams):
    """Custom renderparams class."""

    nodata: Optional[Union[str, int, float]] = Query(
        None,
        title="Tiff Ouptut Nodata value",
        alias="output_nodata",
    )
    compress: Optional[str] = Query(
        None,
        title="Tiff compression schema",
        alias="output_compression",
    )

    def __post_init__(self):
        """post init."""
        if self.nodata is not None:
            self.nodata = numpy.nan if self.nodata == "nan" else float(self.nodata)