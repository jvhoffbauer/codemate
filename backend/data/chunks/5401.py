@dataclass  # type: ignore
class FactoryExtension(metaclass=abc.ABCMeta):
    """Factory Extension."""

    @abc.abstractmethod
    def register(self, factory: "BaseTilerFactory"):
        """Register extension to the factory."""
        ...