    def __tablename__(cls) -> str:
        return humps.depascalize(cls.__name__)