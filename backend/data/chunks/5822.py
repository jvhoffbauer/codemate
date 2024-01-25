    def get_name(self, field: InstrumentedAttribute) -> str:
        return (
            field.key
            if field.class_.__tablename__ == self.__table__.name
            else self._name_format.format(
                model_name=field.class_.__tablename__, field_name=field.key
            )
        )