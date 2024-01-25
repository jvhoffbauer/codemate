def extract(field: str, expr: Union[_ColumnExpressionArgument[Any], Any]) -> Extract:
    return sqlalchemy.extract(field, expr)  # type: ignore[arg-type]