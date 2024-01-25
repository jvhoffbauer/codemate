def any_(expr: Union[_ColumnExpressionArgument[_T], _T]) -> CollectionAggregate[bool]:
    return sqlalchemy.any_(expr)  # type: ignore[arg-type]