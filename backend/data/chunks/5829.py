@lru_cache()
def get_python_type_parse(
    field: Union[InstrumentedAttribute, Column, Label]
) -> Callable:
    try:
        python_type = field.expression.type.python_type
        if issubclass(python_type, datetime.date):
            if issubclass(python_type, datetime.datetime):
                return parse_datetime
            return parse_date
        return python_type
    except NotImplementedError:
        return str