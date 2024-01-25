def all_(expr: Union[_ColumnExpressionArgument[_T], _T]) -> CollectionAggregate[bool]:
    return sqlalchemy.all_(expr)  # type: ignore[arg-type]