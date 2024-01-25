@dataclass
class DefaultDependency:
    """Dataclass with dict unpacking"""

    def keys(self):
        """Return Keys."""
        return self.__dict__.keys()

    def __getitem__(self, key):
        """Return value."""
        return self.__dict__[key]