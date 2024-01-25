    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()