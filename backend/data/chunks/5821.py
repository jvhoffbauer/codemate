    def get_alias(self, field: Union[Column, SqlaInsAttr, Label]) -> str:
        if isinstance(field, Column):
            return (
                field.name
                if field.table.name == self.__table__.name
                else self._alias_format.format(
                    table_name=field.table.name, field_key=field.name
                )
            )
        elif isinstance(field, InstrumentedAttribute):
            return (
                field.key
                if field.class_.__tablename__ == self.__table__.name
                else self._alias_format.format(
                    table_name=field.class_.__tablename__,
                    field_key=field.expression.key,
                )
            )
        elif isinstance(field, Label):
            return field.key
        elif isinstance(field, str) and field in self.__fields__:
            return field
        return ""