@attr.s
class CustomFileBackend(FileBackend):
    """Fake backend to prove we can overwrite min/max zoom."""

    minzoom: Optional[int] = attr.ib(default=None)
    maxzoom: Optional[int] = attr.ib(default=None)

    def __attrs_post_init__(self):
        """Post Init: if not passed in init, try to read from self.input."""
        self.mosaic_def = self.mosaic_def or self._read()
        self.minzoom = self.minzoom or self.mosaic_def.minzoom
        self.maxzoom = self.maxzoom or self.mosaic_def.maxzoom
        self.bounds = self.mosaic_def.bounds