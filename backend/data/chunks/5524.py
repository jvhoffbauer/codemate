    def driver(self):
        """Return rio-tiler image default profile."""
        return ImageDriver[self._name_].value