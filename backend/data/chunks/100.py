def nulls_last(column: Union[_ColumnExpressionArgument[_T], _T]) -> UnaryExpression[_T]:
    return sqlalchemy.nulls_last(column)  # type: ignore[arg-type]