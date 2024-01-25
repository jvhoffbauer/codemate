def not_(clause: Union[_ColumnExpressionArgument[_T], _T]) -> ColumnElement[_T]:
    return sqlalchemy.not_(clause)  # type: ignore[arg-type]