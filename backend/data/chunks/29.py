    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()