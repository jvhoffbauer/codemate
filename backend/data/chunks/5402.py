    @abc.abstractmethod
    def register(self, factory: "BaseTilerFactory"):
        """Register extension to the factory."""
        ...